from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@attr.s(auto_attribs=True)
class Status:
    """
    Attributes:
        user_id (Union[Unset, str]):
        status (Union[Unset, str]):
        manual (Union[Unset, bool]):
        last_activity_at (Union[Unset, int]):
    """

    user_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    manual: Union[Unset, bool] = UNSET
    last_activity_at: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        status = self.status
        manual = self.manual
        last_activity_at = self.last_activity_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if status is not UNSET:
            field_dict["status"] = status
        if manual is not UNSET:
            field_dict["manual"] = manual
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id", UNSET)

        status = d.pop("status", UNSET)

        manual = d.pop("manual", UNSET)

        last_activity_at = d.pop("last_activity_at", UNSET)

        status = cls(
            user_id=user_id,
            status=status,
            manual=manual,
            last_activity_at=last_activity_at,
        )

        status.additional_properties = d
        return status

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
