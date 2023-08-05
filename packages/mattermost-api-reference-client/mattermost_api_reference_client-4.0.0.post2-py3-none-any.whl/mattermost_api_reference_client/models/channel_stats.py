from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelStats")


@attr.s(auto_attribs=True)
class ChannelStats:
    """
    Attributes:
        channel_id (Union[Unset, str]):
        member_count (Union[Unset, int]):
    """

    channel_id: Union[Unset, str] = UNSET
    member_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id
        member_count = self.member_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if member_count is not UNSET:
            field_dict["member_count"] = member_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id", UNSET)

        member_count = d.pop("member_count", UNSET)

        channel_stats = cls(
            channel_id=channel_id,
            member_count=member_count,
        )

        channel_stats.additional_properties = d
        return channel_stats

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
