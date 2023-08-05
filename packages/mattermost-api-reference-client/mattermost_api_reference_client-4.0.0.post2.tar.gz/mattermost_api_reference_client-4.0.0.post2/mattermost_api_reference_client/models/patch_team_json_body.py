from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchTeamJsonBody")


@attr.s(auto_attribs=True)
class PatchTeamJsonBody:
    """
    Attributes:
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        company_name (Union[Unset, str]):
        invite_id (Union[Unset, str]):
        allow_open_invite (Union[Unset, bool]):
    """

    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    invite_id: Union[Unset, str] = UNSET
    allow_open_invite: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        description = self.description
        company_name = self.company_name
        invite_id = self.invite_id
        allow_open_invite = self.allow_open_invite

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if invite_id is not UNSET:
            field_dict["invite_id"] = invite_id
        if allow_open_invite is not UNSET:
            field_dict["allow_open_invite"] = allow_open_invite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name", UNSET)

        description = d.pop("description", UNSET)

        company_name = d.pop("company_name", UNSET)

        invite_id = d.pop("invite_id", UNSET)

        allow_open_invite = d.pop("allow_open_invite", UNSET)

        patch_team_json_body = cls(
            display_name=display_name,
            description=description,
            company_name=company_name,
            invite_id=invite_id,
            allow_open_invite=allow_open_invite,
        )

        patch_team_json_body.additional_properties = d
        return patch_team_json_body

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
