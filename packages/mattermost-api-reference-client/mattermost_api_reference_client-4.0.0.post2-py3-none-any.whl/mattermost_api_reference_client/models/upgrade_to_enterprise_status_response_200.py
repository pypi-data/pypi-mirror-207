from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpgradeToEnterpriseStatusResponse200")


@attr.s(auto_attribs=True)
class UpgradeToEnterpriseStatusResponse200:
    """
    Attributes:
        percentage (Union[Unset, int]): Current percentage of the upgrade
        error (Union[Unset, str]): Error happened during the upgrade
    """

    percentage: Union[Unset, int] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percentage = self.percentage
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percentage = d.pop("percentage", UNSET)

        error = d.pop("error", UNSET)

        upgrade_to_enterprise_status_response_200 = cls(
            percentage=percentage,
            error=error,
        )

        upgrade_to_enterprise_status_response_200.additional_properties = d
        return upgrade_to_enterprise_status_response_200

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
