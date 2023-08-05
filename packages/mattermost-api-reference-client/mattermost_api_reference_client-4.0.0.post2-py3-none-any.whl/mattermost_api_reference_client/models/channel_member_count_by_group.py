from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelMemberCountByGroup")


@attr.s(auto_attribs=True)
class ChannelMemberCountByGroup:
    """An object describing group member information in a channel

    Attributes:
        group_id (Union[Unset, str]): ID of the group
        channel_member_count (Union[Unset, float]): Total number of group members in the channel
        channel_member_timezones_count (Union[Unset, float]): Total number of unique timezones for the group members in
            the channel
    """

    group_id: Union[Unset, str] = UNSET
    channel_member_count: Union[Unset, float] = UNSET
    channel_member_timezones_count: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        channel_member_count = self.channel_member_count
        channel_member_timezones_count = self.channel_member_timezones_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if channel_member_count is not UNSET:
            field_dict["channel_member_count"] = channel_member_count
        if channel_member_timezones_count is not UNSET:
            field_dict["channel_member_timezones_count"] = channel_member_timezones_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("group_id", UNSET)

        channel_member_count = d.pop("channel_member_count", UNSET)

        channel_member_timezones_count = d.pop("channel_member_timezones_count", UNSET)

        channel_member_count_by_group = cls(
            group_id=group_id,
            channel_member_count=channel_member_count,
            channel_member_timezones_count=channel_member_timezones_count,
        )

        channel_member_count_by_group.additional_properties = d
        return channel_member_count_by_group

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
