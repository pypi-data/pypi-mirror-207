from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relational_integrity_check_data import RelationalIntegrityCheckData


T = TypeVar("T", bound="IntegrityCheckResult")


@attr.s(auto_attribs=True)
class IntegrityCheckResult:
    """an object with the result of the integrity check.

    Attributes:
        data (Union[Unset, RelationalIntegrityCheckData]): an object containing the results of a relational integrity
            check.
        err (Union[Unset, str]): a string value set in case of error.
    """

    data: Union[Unset, "RelationalIntegrityCheckData"] = UNSET
    err: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        err = self.err

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if err is not UNSET:
            field_dict["err"] = err

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relational_integrity_check_data import RelationalIntegrityCheckData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, RelationalIntegrityCheckData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RelationalIntegrityCheckData.from_dict(_data)

        err = d.pop("err", UNSET)

        integrity_check_result = cls(
            data=data,
            err=err,
        )

        integrity_check_result.additional_properties = d
        return integrity_check_result

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
