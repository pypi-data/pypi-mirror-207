from __future__ import annotations  # noqa: D100

import logging
from typing import Any

import lightning.pytorch as pl
import torch
from torch import Tensor
from torch import nn


class LightningModule(pl.LightningModule):  # type: ignore
    """Lightning module wrapper for conveniently training SIHL models."""

    def __init__(  # noqa: D107
        self,
        backbone: nn.Module,
        neck: nn.Module | None,
        head: nn.Module,
        optimizer: type[torch.optim.Optimizer] = torch.optim.AdamW,
        optimizer_kwargs: dict[str, Any] | None = None,
        scheduler: type[torch.optim.lr_scheduler._LRScheduler] | None = None,
        scheduler_kwargs: dict[str, Any] | None = None,
    ):
        super().__init__()
        self.optimizer = optimizer
        self.optimizer_kwargs = optimizer_kwargs or {}
        self.scheduler = scheduler
        self.scheduler_kwargs = scheduler_kwargs or {}
        self.backbone = backbone
        self.neck = neck or nn.Identity()
        self.head = head

    def forward(self, input: Tensor) -> tuple[Tensor, ...]:  # noqa: D102
        return self.head(self.neck(self.backbone(input)))  # type: ignore

    def training_step(  # noqa: D102
        self, batch: tuple[Tensor, Any], batch_idx: int
    ) -> Tensor:
        x, *y = batch
        head_inputs = self.neck(self.backbone(x))
        loss, metrics = self.head.training_step(head_inputs, *y)  # type: ignore
        self.log("train/loss", loss, on_epoch=False, on_step=True, prog_bar=True)
        self.log_dict(metrics, on_epoch=False, on_step=True, prog_bar=True)
        scheduler = self.lr_schedulers()
        if scheduler:
            scheduler.step()
            lr = scheduler.get_last_lr()[0]
            self.log("lr", lr, on_epoch=False, on_step=True, prog_bar=True)
        return loss  # type: ignore

    def validation_step(  # noqa: D102
        self, batch: tuple[Tensor, Any], batch_idx: int
    ) -> Tensor:
        x, *y = batch
        head_inputs = self.neck(self.backbone(x))
        loss, metrics = self.head.validation_step(head_inputs, *y)  # type: ignore
        self.log("valid/loss", loss, on_epoch=False, on_step=True, prog_bar=True)
        self.log_dict(metrics, on_epoch=False, on_step=True, prog_bar=True)
        return loss  # type: ignore

    def configure_optimizers(  # noqa: D102
        self,
    ) -> (
        torch.optim.Optimizer
        | tuple[
            list[torch.optim.Optimizer], list[torch.optim.lr_scheduler._LRScheduler]
        ]
    ):
        optimizer = self.optimizer(self.parameters(), **self.optimizer_kwargs)
        if self.scheduler:
            scheduler = self.scheduler(optimizer, **self.scheduler_kwargs)
            return [optimizer], [scheduler]
        return optimizer

    def on_validation_start(self) -> None:  # noqa: D102
        try:
            self.head.on_validation_start()  # type: ignore
        except Exception as e:
            logging.warn(e)
            pass

    def on_validation_epoch_end(self) -> None:  # noqa: D102
        try:
            val_metrics = self.head.on_validation_end()  # type: ignore
            self.log_dict(val_metrics, on_epoch=True, on_step=False, prog_bar=True)
        except Exception as e:
            logging.warn(e)
            pass
