from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentConfigMetricsSettings")


@attr.s(auto_attribs=True)
class EnvironmentConfigMetricsSettings:
    """
    Attributes:
        enable (Union[Unset, bool]):
        block_profile_rate (Union[Unset, bool]):
        listen_address (Union[Unset, bool]):
    """

    enable: Union[Unset, bool] = UNSET
    block_profile_rate: Union[Unset, bool] = UNSET
    listen_address: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        block_profile_rate = self.block_profile_rate
        listen_address = self.listen_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["Enable"] = enable
        if block_profile_rate is not UNSET:
            field_dict["BlockProfileRate"] = block_profile_rate
        if listen_address is not UNSET:
            field_dict["ListenAddress"] = listen_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("Enable", UNSET)

        block_profile_rate = d.pop("BlockProfileRate", UNSET)

        listen_address = d.pop("ListenAddress", UNSET)

        environment_config_metrics_settings = cls(
            enable=enable,
            block_profile_rate=block_profile_rate,
            listen_address=listen_address,
        )

        environment_config_metrics_settings.additional_properties = d
        return environment_config_metrics_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
