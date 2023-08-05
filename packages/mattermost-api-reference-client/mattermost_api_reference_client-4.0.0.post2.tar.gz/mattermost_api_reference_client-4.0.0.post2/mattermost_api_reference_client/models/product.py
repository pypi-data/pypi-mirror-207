from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_on import AddOn


T = TypeVar("T", bound="Product")


@attr.s(auto_attribs=True)
class Product:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        price_per_seat (Union[Unset, str]):
        add_ons (Union[Unset, List['AddOn']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    price_per_seat: Union[Unset, str] = UNSET
    add_ons: Union[Unset, List["AddOn"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        price_per_seat = self.price_per_seat
        add_ons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.add_ons, Unset):
            add_ons = []
            for add_ons_item_data in self.add_ons:
                add_ons_item = add_ons_item_data.to_dict()

                add_ons.append(add_ons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if price_per_seat is not UNSET:
            field_dict["price_per_seat"] = price_per_seat
        if add_ons is not UNSET:
            field_dict["add_ons"] = add_ons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.add_on import AddOn

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        price_per_seat = d.pop("price_per_seat", UNSET)

        add_ons = []
        _add_ons = d.pop("add_ons", UNSET)
        for add_ons_item_data in _add_ons or []:
            add_ons_item = AddOn.from_dict(add_ons_item_data)

            add_ons.append(add_ons_item)

        product = cls(
            id=id,
            name=name,
            description=description,
            price_per_seat=price_per_seat,
            add_ons=add_ons,
        )

        product.additional_properties = d
        return product

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
