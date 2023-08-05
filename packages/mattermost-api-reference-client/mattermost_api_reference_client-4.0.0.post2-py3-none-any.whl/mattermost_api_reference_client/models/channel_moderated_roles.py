from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_moderated_role import ChannelModeratedRole


T = TypeVar("T", bound="ChannelModeratedRoles")


@attr.s(auto_attribs=True)
class ChannelModeratedRoles:
    """
    Attributes:
        guests (Union[Unset, ChannelModeratedRole]):
        members (Union[Unset, ChannelModeratedRole]):
    """

    guests: Union[Unset, "ChannelModeratedRole"] = UNSET
    members: Union[Unset, "ChannelModeratedRole"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guests: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guests, Unset):
            guests = self.guests.to_dict()

        members: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guests is not UNSET:
            field_dict["guests"] = guests
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.channel_moderated_role import ChannelModeratedRole

        d = src_dict.copy()
        _guests = d.pop("guests", UNSET)
        guests: Union[Unset, ChannelModeratedRole]
        if isinstance(_guests, Unset):
            guests = UNSET
        else:
            guests = ChannelModeratedRole.from_dict(_guests)

        _members = d.pop("members", UNSET)
        members: Union[Unset, ChannelModeratedRole]
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = ChannelModeratedRole.from_dict(_members)

        channel_moderated_roles = cls(
            guests=guests,
            members=members,
        )

        channel_moderated_roles.additional_properties = d
        return channel_moderated_roles

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
