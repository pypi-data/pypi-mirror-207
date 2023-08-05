from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataRetentionPolicy")


@attr.s(auto_attribs=True)
class DataRetentionPolicy:
    """
    Attributes:
        display_name (Union[Unset, str]): The display name for this retention policy.
        post_duration (Union[Unset, int]): The number of days a message will be retained before being deleted by this
            policy. If this value is less than 0, the policy has infinite retention (i.e. messages are never deleted).
        id (Union[Unset, str]): The ID of this retention policy.
    """

    display_name: Union[Unset, str] = UNSET
    post_duration: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        post_duration = self.post_duration
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if post_duration is not UNSET:
            field_dict["post_duration"] = post_duration
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name", UNSET)

        post_duration = d.pop("post_duration", UNSET)

        id = d.pop("id", UNSET)

        data_retention_policy = cls(
            display_name=display_name,
            post_duration=post_duration,
            id=id,
        )

        data_retention_policy.additional_properties = d
        return data_retention_policy

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
