from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLineItem")


@attr.s(auto_attribs=True)
class InvoiceLineItem:
    """
    Attributes:
        price_id (Union[Unset, str]):
        total (Union[Unset, int]):
        quantity (Union[Unset, int]):
        price_per_unit (Union[Unset, int]):
        description (Union[Unset, str]):
        metadata (Union[Unset, List[str]]):
    """

    price_id: Union[Unset, str] = UNSET
    total: Union[Unset, int] = UNSET
    quantity: Union[Unset, int] = UNSET
    price_per_unit: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    metadata: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        price_id = self.price_id
        total = self.total
        quantity = self.quantity
        price_per_unit = self.price_per_unit
        description = self.description
        metadata: Union[Unset, List[str]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_id is not UNSET:
            field_dict["price_id"] = price_id
        if total is not UNSET:
            field_dict["total"] = total
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price_per_unit is not UNSET:
            field_dict["price_per_unit"] = price_per_unit
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        price_id = d.pop("price_id", UNSET)

        total = d.pop("total", UNSET)

        quantity = d.pop("quantity", UNSET)

        price_per_unit = d.pop("price_per_unit", UNSET)

        description = d.pop("description", UNSET)

        metadata = cast(List[str], d.pop("metadata", UNSET))

        invoice_line_item = cls(
            price_id=price_id,
            total=total,
            quantity=quantity,
            price_per_unit=price_per_unit,
            description=description,
            metadata=metadata,
        )

        invoice_line_item.additional_properties = d
        return invoice_line_item

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
