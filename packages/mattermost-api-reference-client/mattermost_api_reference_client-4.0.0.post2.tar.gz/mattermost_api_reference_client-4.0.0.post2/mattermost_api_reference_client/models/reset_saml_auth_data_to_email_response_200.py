from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetSamlAuthDataToEmailResponse200")


@attr.s(auto_attribs=True)
class ResetSamlAuthDataToEmailResponse200:
    """
    Attributes:
        num_affected (Union[Unset, int]): The number of users whose AuthData field was reset.
    """

    num_affected: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_affected = self.num_affected

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_affected is not UNSET:
            field_dict["num_affected"] = num_affected

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        num_affected = d.pop("num_affected", UNSET)

        reset_saml_auth_data_to_email_response_200 = cls(
            num_affected=num_affected,
        )

        reset_saml_auth_data_to_email_response_200.additional_properties = d
        return reset_saml_auth_data_to_email_response_200

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
