from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelUnread")


@attr.s(auto_attribs=True)
class ChannelUnread:
    """
    Attributes:
        team_id (Union[Unset, str]):
        channel_id (Union[Unset, str]):
        msg_count (Union[Unset, int]):
        mention_count (Union[Unset, int]):
    """

    team_id: Union[Unset, str] = UNSET
    channel_id: Union[Unset, str] = UNSET
    msg_count: Union[Unset, int] = UNSET
    mention_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        channel_id = self.channel_id
        msg_count = self.msg_count
        mention_count = self.mention_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if msg_count is not UNSET:
            field_dict["msg_count"] = msg_count
        if mention_count is not UNSET:
            field_dict["mention_count"] = mention_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("team_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        msg_count = d.pop("msg_count", UNSET)

        mention_count = d.pop("mention_count", UNSET)

        channel_unread = cls(
            team_id=team_id,
            channel_id=channel_id,
            msg_count=msg_count,
            mention_count=mention_count,
        )

        channel_unread.additional_properties = d
        return channel_unread

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
