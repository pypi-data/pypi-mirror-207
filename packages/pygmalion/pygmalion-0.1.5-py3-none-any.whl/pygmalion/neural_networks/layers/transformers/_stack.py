import torch
from typing import Optional, List, Tuple, Sequence
from ._multihead_attention import ATTENTION_TYPE
from ._stages import TransformerEncoderStage, TransformerDecoderStage
from torch.utils.checkpoint import checkpoint


class TransformerEncoder(torch.nn.Module):
    """
    A transformer encoder is a sequence of TransformerEncoderStage
    """

    def __init__(self, n_stages: int, projection_dim: int, n_heads: int,
                 dropout: Optional[float] = None, activation: str = "relu",
                 RPE_radius: Optional[int] = None, attention_type: ATTENTION_TYPE = "scaled dot product",
                 low_memory: bool = True):
        super().__init__()
        self.stages: Sequence[TransformerEncoderStage] = torch.nn.ModuleList()
        self.low_memory = low_memory
        for stage in range(n_stages):
            self.stages.append(TransformerEncoderStage(projection_dim, n_heads,
                                                       dropout=dropout, activation=activation,
                                                       RPE_radius=RPE_radius,
                                                       attention_type=attention_type))

    def forward(self, X: torch.Tensor, padding_mask: Optional[torch.Tensor] = None):
        """
        Parameter
        ---------
        X : torch.Tensor
            Tensor of shape (N, L, D) with
            * N sentences count
            * L sequence length
            * D number of features
        padding_mask : torch.tensor or None
            tensor of booleans of shape (N, L) of tokens to ignore

        Returns
        -------
        torch.Tensor
            tensor of shape (N, L, D)
        """
        for stage in self.stages:
            if self.low_memory and self.training:
                X = checkpoint(stage, X, padding_mask)
            else:
                X = stage(X, padding_mask)
        return X


class TransformerDecoder(torch.nn.Module):
    """
    A transformer decoder is a sequence of TransformerDecoderStage
    """

    def __init__(self, n_stages: int, projection_dim: int, n_heads: int,
                 dropout: Optional[float] = None, activation: str = "relu",
                 RPE_radius: Optional[int] = None, attention_type: ATTENTION_TYPE = "scaled dot product",
                 low_memory: bool = True):
        super().__init__()
        self.stages: Sequence[TransformerDecoderStage] = torch.nn.ModuleList()
        self.low_memory = low_memory
        for stage in range(n_stages):
            self.stages.append(TransformerDecoderStage(projection_dim, n_heads,
                                                       dropout=dropout, activation=activation,
                                                       RPE_radius=RPE_radius,
                                                       attention_type=attention_type))

    def forward(self, Y: torch.Tensor, encoded: torch.Tensor,
                encoded_padding_mask: Optional[torch.Tensor] = None):
        """
        Parameter
        ---------
        Y : torch.Tensor
            Tensor of shape (N, Lq, D)
        encoded : torch.Tensor
            Tensor of shape (N, Lk, D)
        encoded_padding_mask : torch.Tensor or None
            mask of shape (N, Lk)

        Returns
        -------
        torch.Tensor
            tensor of shape (N, L, D)
        """
        for stage in self.stages:
            if self.low_memory and self.training:
                Y = checkpoint(stage, Y, encoded, encoded_padding_mask)
            else:
                Y = stage(Y, encoded, encoded_padding_mask)
        return Y

    def predict(self, intermediate: List[torch.Tensor],
                Q: torch.Tensor, encoded: torch.Tensor,
                encoded_padding_mask: Optional[torch.Tensor]
                ) -> Tuple[List[torch.Tensor], torch.Tensor]:
        """
        Efficiently predict the next representation of a new predicted vector 'Q',
        and feed the tensors of previously predicted tensors intermediate
        representations 'intermediate'.

        Parameter
        ---------
        intermediate : torch.Tensor
            Tensor of shape (N, Lq-1, D)
        Q : torch.Tensor
            Tensor of shape (N, 1, D)
        encoded : torch.Tensor
            Tensor of shape (N, Lk, D)
        encoded_padding_mask : torch.Tensor or None
            mask of shape (N, Lk)

        Returns
        -------
        tuple :
            tuple of updated (intermediate, Q)
        """
        assert not self.training
        new = []
        for stage, rep in zip(self.stages, intermediate):
            Y = torch.cat([rep, Q], dim=1)
            new.append(Y)
            Q = stage.predict(Y, encoded, encoded_padding_mask)
        return new, Q
