from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethod")


@attr.s(auto_attribs=True)
class PaymentMethod:
    """
    Attributes:
        type (Union[Unset, str]):
        last_four (Union[Unset, int]):
        exp_month (Union[Unset, int]):
        exp_year (Union[Unset, int]):
        card_brand (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    last_four: Union[Unset, int] = UNSET
    exp_month: Union[Unset, int] = UNSET
    exp_year: Union[Unset, int] = UNSET
    card_brand: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        last_four = self.last_four
        exp_month = self.exp_month
        exp_year = self.exp_year
        card_brand = self.card_brand
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if last_four is not UNSET:
            field_dict["last_four"] = last_four
        if exp_month is not UNSET:
            field_dict["exp_month"] = exp_month
        if exp_year is not UNSET:
            field_dict["exp_year"] = exp_year
        if card_brand is not UNSET:
            field_dict["card_brand"] = card_brand
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        last_four = d.pop("last_four", UNSET)

        exp_month = d.pop("exp_month", UNSET)

        exp_year = d.pop("exp_year", UNSET)

        card_brand = d.pop("card_brand", UNSET)

        name = d.pop("name", UNSET)

        payment_method = cls(
            type=type,
            last_four=last_four,
            exp_month=exp_month,
            exp_year=exp_year,
            card_brand=card_brand,
            name=name,
        )

        payment_method.additional_properties = d
        return payment_method

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
