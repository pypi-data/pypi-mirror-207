from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigClusterSettings")


@attr.s(auto_attribs=True)
class ConfigClusterSettings:
    """
    Attributes:
        enable (Union[Unset, bool]):
        inter_node_listen_address (Union[Unset, str]):
        inter_node_urls (Union[Unset, List[str]]):
    """

    enable: Union[Unset, bool] = UNSET
    inter_node_listen_address: Union[Unset, str] = UNSET
    inter_node_urls: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable
        inter_node_listen_address = self.inter_node_listen_address
        inter_node_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.inter_node_urls, Unset):
            inter_node_urls = self.inter_node_urls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["Enable"] = enable
        if inter_node_listen_address is not UNSET:
            field_dict["InterNodeListenAddress"] = inter_node_listen_address
        if inter_node_urls is not UNSET:
            field_dict["InterNodeUrls"] = inter_node_urls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("Enable", UNSET)

        inter_node_listen_address = d.pop("InterNodeListenAddress", UNSET)

        inter_node_urls = cast(List[str], d.pop("InterNodeUrls", UNSET))

        config_cluster_settings = cls(
            enable=enable,
            inter_node_listen_address=inter_node_listen_address,
            inter_node_urls=inter_node_urls,
        )

        config_cluster_settings.additional_properties = d
        return config_cluster_settings

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
