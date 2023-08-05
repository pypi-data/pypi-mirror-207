from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataRetentionPolicyWithTeamAndChannelIds")


@attr.s(auto_attribs=True)
class DataRetentionPolicyWithTeamAndChannelIds:
    """
    Attributes:
        display_name (Union[Unset, str]): The display name for this retention policy.
        post_duration (Union[Unset, int]): The number of days a message will be retained before being deleted by this
            policy. If this value is less than 0, the policy has infinite retention (i.e. messages are never deleted).
        team_ids (Union[Unset, List[str]]): The IDs of the teams to which this policy should be applied.
        channel_ids (Union[Unset, List[str]]): The IDs of the channels to which this policy should be applied.
    """

    display_name: Union[Unset, str] = UNSET
    post_duration: Union[Unset, int] = UNSET
    team_ids: Union[Unset, List[str]] = UNSET
    channel_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        post_duration = self.post_duration
        team_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        channel_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.channel_ids, Unset):
            channel_ids = self.channel_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if post_duration is not UNSET:
            field_dict["post_duration"] = post_duration
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if channel_ids is not UNSET:
            field_dict["channel_ids"] = channel_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name", UNSET)

        post_duration = d.pop("post_duration", UNSET)

        team_ids = cast(List[str], d.pop("team_ids", UNSET))

        channel_ids = cast(List[str], d.pop("channel_ids", UNSET))

        data_retention_policy_with_team_and_channel_ids = cls(
            display_name=display_name,
            post_duration=post_duration,
            team_ids=team_ids,
            channel_ids=channel_ids,
        )

        data_retention_policy_with_team_and_channel_ids.additional_properties = d
        return data_retention_policy_with_team_and_channel_ids

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
