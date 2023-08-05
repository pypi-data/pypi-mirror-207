from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPGroup")


@attr.s(auto_attribs=True)
class LDAPGroup:
    """A LDAP group

    Attributes:
        has_syncables (Union[Unset, bool]):
        mattermost_group_id (Union[Unset, str]):
        primary_key (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    has_syncables: Union[Unset, bool] = UNSET
    mattermost_group_id: Union[Unset, str] = UNSET
    primary_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_syncables = self.has_syncables
        mattermost_group_id = self.mattermost_group_id
        primary_key = self.primary_key
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_syncables is not UNSET:
            field_dict["has_syncables"] = has_syncables
        if mattermost_group_id is not UNSET:
            field_dict["mattermost_group_id"] = mattermost_group_id
        if primary_key is not UNSET:
            field_dict["primary_key"] = primary_key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_syncables = d.pop("has_syncables", UNSET)

        mattermost_group_id = d.pop("mattermost_group_id", UNSET)

        primary_key = d.pop("primary_key", UNSET)

        name = d.pop("name", UNSET)

        ldap_group = cls(
            has_syncables=has_syncables,
            mattermost_group_id=mattermost_group_id,
            primary_key=primary_key,
            name=name,
        )

        ldap_group.additional_properties = d
        return ldap_group

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
