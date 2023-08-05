from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAcknowledgement")


@attr.s(auto_attribs=True)
class PostAcknowledgement:
    """
    Attributes:
        user_id (Union[Unset, str]): The ID of the user that made this acknowledgement.
        post_id (Union[Unset, str]): The ID of the post to which this acknowledgement was made.
        acknowledged_at (Union[Unset, int]): The time in milliseconds in which this acknowledgement was made.
    """

    user_id: Union[Unset, str] = UNSET
    post_id: Union[Unset, str] = UNSET
    acknowledged_at: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        post_id = self.post_id
        acknowledged_at = self.acknowledged_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id", UNSET)

        post_id = d.pop("post_id", UNSET)

        acknowledged_at = d.pop("acknowledged_at", UNSET)

        post_acknowledgement = cls(
            user_id=user_id,
            post_id=post_id,
            acknowledged_at=acknowledged_at,
        )

        post_acknowledgement.additional_properties = d
        return post_acknowledgement

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
