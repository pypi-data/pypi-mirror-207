from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerBusy")


@attr.s(auto_attribs=True)
class ServerBusy:
    """
    Attributes:
        busy (Union[Unset, bool]): True if the server is marked as busy (under high load)
        expires (Union[Unset, int]): timestamp - number of seconds since Jan 1, 1970 UTC.
    """

    busy: Union[Unset, bool] = UNSET
    expires: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        busy = self.busy
        expires = self.expires

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if busy is not UNSET:
            field_dict["busy"] = busy
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        busy = d.pop("busy", UNSET)

        expires = d.pop("expires", UNSET)

        server_busy = cls(
            busy=busy,
            expires=expires,
        )

        server_busy.additional_properties = d
        return server_busy

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
