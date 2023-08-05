from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePlaybookJsonBodyChecklistsItemItemsItem")


@attr.s(auto_attribs=True)
class CreatePlaybookJsonBodyChecklistsItemItemsItem:
    """
    Attributes:
        title (str): The title of the checklist item. Example: Gather information from customer..
        command (Union[Unset, str]): The slash command associated with this item. If the item has no slash command
            associated, this is an empty string Example: /opsgenie on-call.
        description (Union[Unset, str]): A detailed description of the checklist item, formatted with Markdown. Example:
            Ask the customer for more information in [Zendesk](https://www.zendesk.com/)..
    """

    title: str
    command: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        command = self.command
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        command = d.pop("command", UNSET)

        description = d.pop("description", UNSET)

        create_playbook_json_body_checklists_item_items_item = cls(
            title=title,
            command=command,
            description=description,
        )

        create_playbook_json_body_checklists_item_items_item.additional_properties = d
        return create_playbook_json_body_checklists_item_items_item

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
