from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TermsOfService")


@attr.s(auto_attribs=True)
class TermsOfService:
    """
    Attributes:
        id (Union[Unset, str]): The unique identifier of the terms of service.
        create_at (Union[Unset, int]): The time at which the terms of service was created.
        user_id (Union[Unset, str]): The unique identifier of the user who created these terms of service.
        text (Union[Unset, str]): The text of terms of service. Supports Markdown.
    """

    id: Union[Unset, str] = UNSET
    create_at: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        create_at = self.create_at
        user_id = self.user_id
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        create_at = d.pop("create_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        text = d.pop("text", UNSET)

        terms_of_service = cls(
            id=id,
            create_at=create_at,
            user_id=user_id,
            text=text,
        )

        terms_of_service.additional_properties = d
        return terms_of_service

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
