from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaybookAutofollows")


@attr.s(auto_attribs=True)
class PlaybookAutofollows:
    """
    Attributes:
        total_count (Union[Unset, int]): The total number of users who marked this playbook to auto-follow runs.
            Example: 12.
        items (Union[Unset, List[str]]): The user IDs of who marked this playbook to auto-follow.
    """

    total_count: Union[Unset, int] = UNSET
    items: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        items: Union[Unset, List[str]] = UNSET
        if not isinstance(self.items, Unset):
            items = self.items

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count", UNSET)

        items = cast(List[str], d.pop("items", UNSET))

        playbook_autofollows = cls(
            total_count=total_count,
            items=items,
        )

        playbook_autofollows.additional_properties = d
        return playbook_autofollows

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
