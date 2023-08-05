from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppError")


@attr.s(auto_attribs=True)
class AppError:
    """
    Attributes:
        status_code (Union[Unset, int]):
        id (Union[Unset, str]):
        message (Union[Unset, str]):
        request_id (Union[Unset, str]):
    """

    status_code: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_code = self.status_code
        id = self.id
        message = self.message
        request_id = self.request_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_code = d.pop("status_code", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        request_id = d.pop("request_id", UNSET)

        app_error = cls(
            status_code=status_code,
            id=id,
            message=message,
            request_id=request_id,
        )

        app_error.additional_properties = d
        return app_error

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
