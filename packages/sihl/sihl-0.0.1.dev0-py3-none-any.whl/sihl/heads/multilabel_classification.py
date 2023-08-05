from __future__ import annotations  # noqa: D100

import torch
from torch import Tensor
from torch import nn
from torchmetrics.classification import MultilabelAccuracy
from torchmetrics.classification import MultilabelPrecision
from torchmetrics.classification import MultilabelRecall


class MultilabelClassification(nn.Module):  # noqa: D101
    def __init__(  # noqa: D107
        self,
        in_channels: int,
        num_classes: int,
        label_weights: list[float] | None = None,
    ) -> None:
        super().__init__()
        self.num_classes = num_classes
        self.label_weights = torch.tensor(label_weights) if label_weights else None
        self.net = nn.Sequential(
            nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(in_channels, num_classes)
        )

    def forward(self, inputs: list[Tensor]) -> tuple[Tensor, Tensor]:  # noqa: D102
        scores, classes = torch.sort(
            torch.sigmoid(self.net(inputs[-1])), descending=True
        )
        return scores, classes

    def training_step(  # noqa: D102
        self, inputs: list[Tensor], labels: Tensor
    ) -> tuple[Tensor, dict[str, float]]:
        logits = self.net(inputs[-1])
        loss = torch.nn.functional.binary_cross_entropy_with_logits(
            logits, labels, pos_weight=self.label_weights
        )
        return loss, {}

    def on_validation_start(self) -> None:  # noqa: D102
        self.accuracy_computer = MultilabelAccuracy(num_labels=self.num_classes)
        self.precision_computer = MultilabelPrecision(num_labels=self.num_classes)
        self.recall_computer = MultilabelRecall(num_labels=self.num_classes)

    def validation_step(  # noqa: D102
        self, inputs: list[Tensor], labels: Tensor
    ) -> tuple[Tensor, dict[str, float]]:
        self.accuracy_computer = self.accuracy_computer.to(inputs[-1].device)
        self.precision_computer = self.precision_computer.to(inputs[-1].device)
        self.recall_computer = self.recall_computer.to(inputs[-1].device)
        logits = self.net(inputs[-1])
        loss = torch.nn.functional.binary_cross_entropy_with_logits(
            logits, labels, pos_weight=self.label_weights
        )
        self.accuracy_computer.update(logits, labels)
        self.precision_computer.update(logits, labels)
        self.recall_computer.update(logits, labels)
        return loss, {}

    def on_validation_end(self) -> dict[str, float]:  # noqa: D102
        return {
            "accuracy": self.accuracy_computer.compute().item(),
            "precision": self.precision_computer.compute().item(),
            "recall": self.recall_computer.compute().item(),
        }
