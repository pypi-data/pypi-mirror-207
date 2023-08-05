from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteClusterInfo")


@attr.s(auto_attribs=True)
class RemoteClusterInfo:
    """
    Attributes:
        display_name (Union[Unset, str]): The display name for the remote cluster
        create_at (Union[Unset, int]): The time in milliseconds a remote cluster was created
        last_ping_at (Union[Unset, int]): The time in milliseconds a remote cluster was last pinged successfully
    """

    display_name: Union[Unset, str] = UNSET
    create_at: Union[Unset, int] = UNSET
    last_ping_at: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        create_at = self.create_at
        last_ping_at = self.last_ping_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if last_ping_at is not UNSET:
            field_dict["last_ping_at"] = last_ping_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name", UNSET)

        create_at = d.pop("create_at", UNSET)

        last_ping_at = d.pop("last_ping_at", UNSET)

        remote_cluster_info = cls(
            display_name=display_name,
            create_at=create_at,
            last_ping_at=last_ping_at,
        )

        remote_cluster_info.additional_properties = d
        return remote_cluster_info

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
