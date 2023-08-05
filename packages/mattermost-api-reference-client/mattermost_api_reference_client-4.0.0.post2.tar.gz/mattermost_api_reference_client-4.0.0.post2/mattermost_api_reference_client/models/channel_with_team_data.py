from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelWithTeamData")


@attr.s(auto_attribs=True)
class ChannelWithTeamData:
    """
    Attributes:
        id (Union[Unset, str]):
        create_at (Union[Unset, int]): The time in milliseconds a channel was created
        update_at (Union[Unset, int]): The time in milliseconds a channel was last updated
        delete_at (Union[Unset, int]): The time in milliseconds a channel was deleted
        team_id (Union[Unset, str]):
        type (Union[Unset, str]):
        display_name (Union[Unset, str]):
        name (Union[Unset, str]):
        header (Union[Unset, str]):
        purpose (Union[Unset, str]):
        last_post_at (Union[Unset, int]): The time in milliseconds of the last post of a channel
        total_msg_count (Union[Unset, int]):
        extra_update_at (Union[Unset, int]): Deprecated in Mattermost 5.0 release
        creator_id (Union[Unset, str]):
        team_display_name (Union[Unset, str]): The display name of the team to which this channel belongs.
        team_name (Union[Unset, str]): The name of the team to which this channel belongs.
        team_update_at (Union[Unset, int]): The time at which the team to which this channel belongs was last updated.
        policy_id (Union[Unset, str]): The data retention policy to which this team has been assigned. If no such policy
            exists, or the caller does not have the `sysconsole_read_compliance_data_retention` permission, this field will
            be null.
    """

    id: Union[Unset, str] = UNSET
    create_at: Union[Unset, int] = UNSET
    update_at: Union[Unset, int] = UNSET
    delete_at: Union[Unset, int] = UNSET
    team_id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    header: Union[Unset, str] = UNSET
    purpose: Union[Unset, str] = UNSET
    last_post_at: Union[Unset, int] = UNSET
    total_msg_count: Union[Unset, int] = UNSET
    extra_update_at: Union[Unset, int] = UNSET
    creator_id: Union[Unset, str] = UNSET
    team_display_name: Union[Unset, str] = UNSET
    team_name: Union[Unset, str] = UNSET
    team_update_at: Union[Unset, int] = UNSET
    policy_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        create_at = self.create_at
        update_at = self.update_at
        delete_at = self.delete_at
        team_id = self.team_id
        type = self.type
        display_name = self.display_name
        name = self.name
        header = self.header
        purpose = self.purpose
        last_post_at = self.last_post_at
        total_msg_count = self.total_msg_count
        extra_update_at = self.extra_update_at
        creator_id = self.creator_id
        team_display_name = self.team_display_name
        team_name = self.team_name
        team_update_at = self.team_update_at
        policy_id = self.policy_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if update_at is not UNSET:
            field_dict["update_at"] = update_at
        if delete_at is not UNSET:
            field_dict["delete_at"] = delete_at
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if type is not UNSET:
            field_dict["type"] = type
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if header is not UNSET:
            field_dict["header"] = header
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if last_post_at is not UNSET:
            field_dict["last_post_at"] = last_post_at
        if total_msg_count is not UNSET:
            field_dict["total_msg_count"] = total_msg_count
        if extra_update_at is not UNSET:
            field_dict["extra_update_at"] = extra_update_at
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if team_display_name is not UNSET:
            field_dict["team_display_name"] = team_display_name
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if team_update_at is not UNSET:
            field_dict["team_update_at"] = team_update_at
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        create_at = d.pop("create_at", UNSET)

        update_at = d.pop("update_at", UNSET)

        delete_at = d.pop("delete_at", UNSET)

        team_id = d.pop("team_id", UNSET)

        type = d.pop("type", UNSET)

        display_name = d.pop("display_name", UNSET)

        name = d.pop("name", UNSET)

        header = d.pop("header", UNSET)

        purpose = d.pop("purpose", UNSET)

        last_post_at = d.pop("last_post_at", UNSET)

        total_msg_count = d.pop("total_msg_count", UNSET)

        extra_update_at = d.pop("extra_update_at", UNSET)

        creator_id = d.pop("creator_id", UNSET)

        team_display_name = d.pop("team_display_name", UNSET)

        team_name = d.pop("team_name", UNSET)

        team_update_at = d.pop("team_update_at", UNSET)

        policy_id = d.pop("policy_id", UNSET)

        channel_with_team_data = cls(
            id=id,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
            team_id=team_id,
            type=type,
            display_name=display_name,
            name=name,
            header=header,
            purpose=purpose,
            last_post_at=last_post_at,
            total_msg_count=total_msg_count,
            extra_update_at=extra_update_at,
            creator_id=creator_id,
            team_display_name=team_display_name,
            team_name=team_name,
            team_update_at=team_update_at,
            policy_id=policy_id,
        )

        channel_with_team_data.additional_properties = d
        return channel_with_team_data

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
