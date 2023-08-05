from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ItemSetAssigneeJsonBody")


@attr.s(auto_attribs=True)
class ItemSetAssigneeJsonBody:
    """
    Attributes:
        assignee_id (str): The user ID of the new assignee of the item. Example: ruu86intseidqdxjojia41u7l1.
    """

    assignee_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee_id = self.assignee_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignee_id": assignee_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assignee_id = d.pop("assignee_id")

        item_set_assignee_json_body = cls(
            assignee_id=assignee_id,
        )

        item_set_assignee_json_body.additional_properties = d
        return item_set_assignee_json_body

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
