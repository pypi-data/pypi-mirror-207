from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentConfigComplianceSettings")


@attr.s(auto_attribs=True)
class EnvironmentConfigComplianceSettings:
    """
    Attributes:
        enable (Union[Unset, bool]):
        directory (Union[Unset, bool]):
        enable_daily (Union[Unset, bool]):
    """

    enable: Union[Unset, bool] = UNSET
    directory: Union[Unset, bool] = UNSET
    enable_daily: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        directory = self.directory
        enable_daily = self.enable_daily

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["Enable"] = enable
        if directory is not UNSET:
            field_dict["Directory"] = directory
        if enable_daily is not UNSET:
            field_dict["EnableDaily"] = enable_daily

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("Enable", UNSET)

        directory = d.pop("Directory", UNSET)

        enable_daily = d.pop("EnableDaily", UNSET)

        environment_config_compliance_settings = cls(
            enable=enable,
            directory=directory,
            enable_daily=enable_daily,
        )

        environment_config_compliance_settings.additional_properties = d
        return environment_config_compliance_settings

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
