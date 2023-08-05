from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """
    Attributes:
        error (str): A message with the error description. Example: Error retrieving the resource..
        details (str): Further details on where and why this error happened. Example: Specific details about the error,
            depending on the case..
    """

    error: str
    details: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        details = self.details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "details": details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error")

        details = d.pop("details")

        error = cls(
            error=error,
            details=details,
        )

        error.additional_properties = d
        return error

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
