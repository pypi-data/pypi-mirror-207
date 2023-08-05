from __future__ import annotations  # noqa: D100

import torch
import torchmetrics
from torch import Tensor
from torch import nn


class BinaryClassification(nn.Module):  # noqa: D101
    def __init__(self, in_channels: int) -> None:  # noqa: D107
        super().__init__()
        self.net = nn.Sequential(
            nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(in_channels, 1)
        )

    def forward(self, inputs: list[Tensor]) -> tuple[Tensor, Tensor]:  # noqa: D102
        scores = torch.sigmoid(self.net(inputs[-1])).squeeze(-1)
        return scores, scores > 0.5

    def training_step(  # noqa: D102
        self, inputs: list[Tensor], categories: Tensor
    ) -> tuple[Tensor, dict[str, float]]:
        logits = self.net(inputs[-1]).squeeze(-1)
        targets = categories.to(logits.dtype).to(logits.device)
        loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, targets)
        return loss, {}

    def on_validation_start(self) -> None:  # noqa: D102
        self.accuracy_computer = torchmetrics.classification.BinaryAccuracy()
        self.precision_computer = torchmetrics.classification.BinaryPrecision()
        self.recall_computer = torchmetrics.classification.BinaryRecall()

    def validation_step(  # noqa: D102
        self, inputs: list[Tensor], categories: Tensor
    ) -> tuple[Tensor, dict[str, float]]:
        self.accuracy_computer = self.accuracy_computer.to(inputs[-1].device)
        self.precision_computer = self.precision_computer.to(inputs[-1].device)
        self.recall_computer = self.recall_computer.to(inputs[-1].device)
        logits = self.net(inputs[-1]).squeeze(-1)
        targets = categories.to(logits.dtype).to(logits.device)
        loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, targets)
        self.accuracy_computer.update(logits, targets)
        self.precision_computer.update(logits, targets)
        self.recall_computer.update(logits, targets)
        return loss, {}

    def on_validation_end(self) -> dict[str, float]:  # noqa: D102
        return {
            "accuracy": self.accuracy_computer.compute().item(),
            "precision": self.precision_computer.compute().item(),
            "recall": self.recall_computer.compute().item(),
        }
