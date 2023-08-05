from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccessToken")


@attr.s(auto_attribs=True)
class UserAccessToken:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the token
        token (Union[Unset, str]): The token used for authentication
        user_id (Union[Unset, str]): The user the token authenticates for
        description (Union[Unset, str]): A description of the token usage
    """

    id: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        token = self.token
        user_id = self.user_id
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if token is not UNSET:
            field_dict["token"] = token
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        token = d.pop("token", UNSET)

        user_id = d.pop("user_id", UNSET)

        description = d.pop("description", UNSET)

        user_access_token = cls(
            id=id,
            token=token,
            user_id=user_id,
            description=description,
        )

        user_access_token.additional_properties = d
        return user_access_token

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
