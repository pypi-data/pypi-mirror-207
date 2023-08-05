from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenGraphAudiosItem")


@attr.s(auto_attribs=True)
class OpenGraphAudiosItem:
    """Audio object used in OpenGraph metadata of a webpage

    Attributes:
        url (Union[Unset, str]):
        secure_url (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    url: Union[Unset, str] = UNSET
    secure_url: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        secure_url = self.secure_url
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if secure_url is not UNSET:
            field_dict["secure_url"] = secure_url
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        secure_url = d.pop("secure_url", UNSET)

        type = d.pop("type", UNSET)

        open_graph_audios_item = cls(
            url=url,
            secure_url=secure_url,
            type=type,
        )

        open_graph_audios_item.additional_properties = d
        return open_graph_audios_item

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
