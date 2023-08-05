from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreatePlaybookResponse201")


@attr.s(auto_attribs=True)
class CreatePlaybookResponse201:
    """
    Attributes:
        id (str):  Example: iz0g457ikesz55dhxcfa0fk9yy.
    """

    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        create_playbook_response_201 = cls(
            id=id,
        )

        create_playbook_response_201.additional_properties = d
        return create_playbook_response_201

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
