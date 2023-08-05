from __future__ import annotations  # noqa: D100

from typing import Final

import torch
import torchvision
from torch import Tensor
from torch import fx
from torch import nn
from torch.fx.experimental.optimization import matches_module_pattern
from torch.fx.experimental.optimization import replace_node_module
from torchvision import transforms
from torchvision.models.feature_extraction import create_feature_extractor


@torch.no_grad()
def update_input_channels(  # noqa: D103
    fx_module: fx.GraphModule, in_channels: int  # type: ignore
) -> None:
    modules = dict(fx_module.named_modules())
    for node in fx_module.graph.nodes:
        if matches_module_pattern([nn.Conv2d], node, modules):
            conv = modules[node.args[0].target]
            if conv.in_channels == 3:
                new_conv = nn.Conv2d(
                    in_channels=in_channels,
                    out_channels=conv.out_channels,
                    kernel_size=conv.kernel_size,
                    stride=conv.stride,
                    padding=conv.padding,
                    dilation=conv.dilation,
                    groups=conv.groups,
                    bias=conv.bias,
                    padding_mode=conv.padding_mode,
                )
                weight = conv.weight.clone()
                for channel_idx in range(in_channels):
                    new_conv.weight[:, channel_idx] = weight[:, channel_idx % 3]
                replace_node_module(node.args[0], modules, new_conv)
                node.replace_all_uses_with(node.args[0])
                fx_module.graph.erase_node(node)
                break
    fx_module.recompile()


class TorchvisionBackbone(nn.Module):  # noqa: D101
    all_level_names: Final[dict[str, list[str]]] = {
        "efficientnet_b0": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_b1": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_b2": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_b3": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_b4": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_b5": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_b6": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_b7": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_v2_l": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_v2_m": [f"features.{_}" for _ in (1, 2, 3, 5, 8)],
        "efficientnet_v2_s": [f"features.{_}" for _ in (1, 2, 3, 5, 7)],
        "mnasnet0_5": [f"layers.{_}" for _ in (7, 8, 9, 11, 16)],
        "mnasnet0_75": [f"layers.{_}" for _ in (7, 8, 9, 11, 16)],
        "mnasnet1_0": [f"layers.{_}" for _ in (7, 8, 9, 11, 16)],
        "mnasnet1_3": [f"layers.{_}" for _ in (7, 8, 9, 11, 16)],
        "mobilenet_v2": [f"features.{_}" for _ in (1, 3, 6, 13, 18)],
        "mobilenet_v3_large": [f"features.{_}" for _ in (1, 3, 6, 12, 16)],
        "mobilenet_v3_small": [f"features.{_}" for _ in (0, 1, 3, 8, 12)],
        "resnet101": ["relu"] + [f"layer{_}" for _ in [1, 2, 3, 4]],
        "resnet152": ["relu"] + [f"layer{_}" for _ in [1, 2, 3, 4]],
        "resnet18": ["relu"] + [f"layer{_}" for _ in [1, 2, 3, 4]],
        "resnet34": ["relu"] + [f"layer{_}" for _ in [1, 2, 3, 4]],
        "resnet50": ["relu"] + [f"layer{_}" for _ in [1, 2, 3, 4]],
        "regnet_x_16gf": ["stem"] + [f"trunk_output.block{_}" for _ in [1, 2, 3, 4]],
    }
    min_level: Final[int] = 1
    max_level: Final[int] = 5

    def __init__(  # noqa: D107, C901
        self,
        name: str,
        pretrained: bool = False,
        input_channels: int = 3,
        frozen_levels: int = 0,
    ) -> None:
        super().__init__()
        self.name = name
        try:
            level_names = self.all_level_names[name]
        except KeyError as error:
            raise KeyError(
                f"Architecture {name} is not supported. "  # noqa: S608
                f"Select from {list(self.all_level_names.keys())}"
            ) from error
        self.normalize = (
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            if pretrained and input_channels == 3
            else transforms.Normalize(mean=(0.5,), std=(0.5,))
        )
        torchvision_model = torchvision.models.get_model(
            name, weights="DEFAULT" if pretrained else None
        )
        torchvision_model = create_feature_extractor(torchvision_model, level_names)
        torchvision_model = fx.symbolic_trace(torchvision_model)  # type: ignore
        update_input_channels(torchvision_model, input_channels)
        # freeze modules in first `frozen_levels` levels
        torchvision_model.eval()  # freeze batchnorms
        if frozen_levels < 0:
            for module_name, _ in torchvision_model.named_modules():
                for param in torchvision_model.get_submodule(module_name).parameters():
                    param.requires_grad = False
        elif frozen_levels > 0:
            last_frozen_name = level_names[min(frozen_levels, len(level_names)) - 1]
            last_level_reached = False
            freezing = True
            for module_name, _ in torchvision_model.named_modules():
                if module_name == "":
                    continue
                if module_name == last_frozen_name:
                    last_level_reached = True
                if last_level_reached and last_frozen_name not in module_name:
                    freezing = False
                for param in torchvision_model.get_submodule(module_name).parameters():
                    param.requires_grad = not freezing
        setattr(self, name, torchvision_model)
        self.dummy_input = torch.empty((1, input_channels, 64, 64))
        self.output_channels = [
            _.shape[1] for _ in getattr(self, name)(self.dummy_input).values()
        ]

    def forward(self, x: Tensor) -> list[Tensor]:  # noqa: D102
        assert (  # noqa: S101
            min(x.shape[2:]) >= 64
        ), f"Input resolution must be at least 64x64, got {tuple(x.shape[2:])}"
        return list(getattr(self, self.name)(self.normalize(x)).values())
