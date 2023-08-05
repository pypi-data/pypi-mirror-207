from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentConfigRateLimitSettings")


@attr.s(auto_attribs=True)
class EnvironmentConfigRateLimitSettings:
    """
    Attributes:
        enable (Union[Unset, bool]):
        per_sec (Union[Unset, bool]):
        max_burst (Union[Unset, bool]):
        memory_store_size (Union[Unset, bool]):
        vary_by_remote_addr (Union[Unset, bool]):
        vary_by_header (Union[Unset, bool]):
    """

    enable: Union[Unset, bool] = UNSET
    per_sec: Union[Unset, bool] = UNSET
    max_burst: Union[Unset, bool] = UNSET
    memory_store_size: Union[Unset, bool] = UNSET
    vary_by_remote_addr: Union[Unset, bool] = UNSET
    vary_by_header: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        per_sec = self.per_sec
        max_burst = self.max_burst
        memory_store_size = self.memory_store_size
        vary_by_remote_addr = self.vary_by_remote_addr
        vary_by_header = self.vary_by_header

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["Enable"] = enable
        if per_sec is not UNSET:
            field_dict["PerSec"] = per_sec
        if max_burst is not UNSET:
            field_dict["MaxBurst"] = max_burst
        if memory_store_size is not UNSET:
            field_dict["MemoryStoreSize"] = memory_store_size
        if vary_by_remote_addr is not UNSET:
            field_dict["VaryByRemoteAddr"] = vary_by_remote_addr
        if vary_by_header is not UNSET:
            field_dict["VaryByHeader"] = vary_by_header

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("Enable", UNSET)

        per_sec = d.pop("PerSec", UNSET)

        max_burst = d.pop("MaxBurst", UNSET)

        memory_store_size = d.pop("MemoryStoreSize", UNSET)

        vary_by_remote_addr = d.pop("VaryByRemoteAddr", UNSET)

        vary_by_header = d.pop("VaryByHeader", UNSET)

        environment_config_rate_limit_settings = cls(
            enable=enable,
            per_sec=per_sec,
            max_burst=max_burst,
            memory_store_size=memory_store_size,
            vary_by_remote_addr=vary_by_remote_addr,
            vary_by_header=vary_by_header,
        )

        environment_config_rate_limit_settings.additional_properties = d
        return environment_config_rate_limit_settings

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
