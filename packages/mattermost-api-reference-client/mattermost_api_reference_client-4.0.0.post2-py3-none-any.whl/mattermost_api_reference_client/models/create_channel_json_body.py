from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateChannelJsonBody")


@attr.s(auto_attribs=True)
class CreateChannelJsonBody:
    """
    Attributes:
        team_id (str): The team ID of the team to create the channel on
        name (str): The unique handle for the channel, will be present in the channel URL
        display_name (str): The non-unique UI name for the channel
        type (str): 'O' for a public channel, 'P' for a private channel
        purpose (Union[Unset, str]): A short description of the purpose of the channel
        header (Union[Unset, str]): Markdown-formatted text to display in the header of the channel
    """

    team_id: str
    name: str
    display_name: str
    type: str
    purpose: Union[Unset, str] = UNSET
    header: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        name = self.name
        display_name = self.display_name
        type = self.type
        purpose = self.purpose
        header = self.header

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "name": name,
                "display_name": display_name,
                "type": type,
            }
        )
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if header is not UNSET:
            field_dict["header"] = header

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("team_id")

        name = d.pop("name")

        display_name = d.pop("display_name")

        type = d.pop("type")

        purpose = d.pop("purpose", UNSET)

        header = d.pop("header", UNSET)

        create_channel_json_body = cls(
            team_id=team_id,
            name=name,
            display_name=display_name,
            type=type,
            purpose=purpose,
            header=header,
        )

        create_channel_json_body.additional_properties = d
        return create_channel_json_body

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
