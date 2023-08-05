from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.orphaned_record import OrphanedRecord


T = TypeVar("T", bound="RelationalIntegrityCheckData")


@attr.s(auto_attribs=True)
class RelationalIntegrityCheckData:
    """an object containing the results of a relational integrity check.

    Attributes:
        parent_name (Union[Unset, str]): the name of the parent relation (table).
        child_name (Union[Unset, str]): the name of the child relation (table).
        parent_id_attr (Union[Unset, str]): the name of the attribute (column) containing the parent id.
        child_id_attr (Union[Unset, str]): the name of the attribute (column) containing the child id.
        records (Union[Unset, List['OrphanedRecord']]): the list of orphaned records found.
    """

    parent_name: Union[Unset, str] = UNSET
    child_name: Union[Unset, str] = UNSET
    parent_id_attr: Union[Unset, str] = UNSET
    child_id_attr: Union[Unset, str] = UNSET
    records: Union[Unset, List["OrphanedRecord"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent_name = self.parent_name
        child_name = self.child_name
        parent_id_attr = self.parent_id_attr
        child_id_attr = self.child_id_attr
        records: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()

                records.append(records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_name is not UNSET:
            field_dict["parent_name"] = parent_name
        if child_name is not UNSET:
            field_dict["child_name"] = child_name
        if parent_id_attr is not UNSET:
            field_dict["parent_id_attr"] = parent_id_attr
        if child_id_attr is not UNSET:
            field_dict["child_id_attr"] = child_id_attr
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.orphaned_record import OrphanedRecord

        d = src_dict.copy()
        parent_name = d.pop("parent_name", UNSET)

        child_name = d.pop("child_name", UNSET)

        parent_id_attr = d.pop("parent_id_attr", UNSET)

        child_id_attr = d.pop("child_id_attr", UNSET)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = OrphanedRecord.from_dict(records_item_data)

            records.append(records_item)

        relational_integrity_check_data = cls(
            parent_name=parent_name,
            child_name=child_name,
            parent_id_attr=parent_id_attr,
            child_id_attr=child_id_attr,
            records=records,
        )

        relational_integrity_check_data.additional_properties = d
        return relational_integrity_check_data

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
