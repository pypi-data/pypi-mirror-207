from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.add_checklist_item_json_body_state import AddChecklistItemJsonBodyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddChecklistItemJsonBody")


@attr.s(auto_attribs=True)
class AddChecklistItemJsonBody:
    """
    Attributes:
        title (str): The title of the checklist item. Example: Gather information from customer..
        state (Union[Unset, AddChecklistItemJsonBodyState]): The state of the checklist item. An empty string means that
            the item is not done. Example: closed.
        state_modified (Union[Unset, int]): The timestamp for the latest modification of the item's state, formatted as
            the number of milliseconds since the Unix epoch. It equals 0 if the item was never modified. Example:
            1607774621321.
        assignee_id (Union[Unset, str]): The identifier of the user that has been assigned to complete this item. If the
            item has no assignee, this is an empty string. Example: pisdatkjtdlkdhht2v4inxuzx1.
        assignee_modified (Union[Unset, int]): The timestamp for the latest modification of the item's assignee,
            formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item never got an assignee.
            Example: 1608897821125.
        command (Union[Unset, str]): The slash command associated with this item. If the item has no slash command
            associated, this is an empty string Example: /opsgenie on-call.
        command_last_run (Union[Unset, int]): The timestamp for the latest execution of the item's command, formatted as
            the number of milliseconds since the Unix epoch. It equals 0 if the command was never executed. Example:
            1608552221019.
        description (Union[Unset, str]): A detailed description of the checklist item, formatted with Markdown. Example:
            Ask the customer for more information in [Zendesk](https://www.zendesk.com/)..
    """

    title: str
    state: Union[Unset, AddChecklistItemJsonBodyState] = UNSET
    state_modified: Union[Unset, int] = UNSET
    assignee_id: Union[Unset, str] = UNSET
    assignee_modified: Union[Unset, int] = UNSET
    command: Union[Unset, str] = UNSET
    command_last_run: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_modified = self.state_modified
        assignee_id = self.assignee_id
        assignee_modified = self.assignee_modified
        command = self.command
        command_last_run = self.command_last_run
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if state_modified is not UNSET:
            field_dict["state_modified"] = state_modified
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if assignee_modified is not UNSET:
            field_dict["assignee_modified"] = assignee_modified
        if command is not UNSET:
            field_dict["command"] = command
        if command_last_run is not UNSET:
            field_dict["command_last_run"] = command_last_run
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        _state = d.pop("state", UNSET)
        state: Union[Unset, AddChecklistItemJsonBodyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = AddChecklistItemJsonBodyState(_state)

        state_modified = d.pop("state_modified", UNSET)

        assignee_id = d.pop("assignee_id", UNSET)

        assignee_modified = d.pop("assignee_modified", UNSET)

        command = d.pop("command", UNSET)

        command_last_run = d.pop("command_last_run", UNSET)

        description = d.pop("description", UNSET)

        add_checklist_item_json_body = cls(
            title=title,
            state=state,
            state_modified=state_modified,
            assignee_id=assignee_id,
            assignee_modified=assignee_modified,
            command=command,
            command_last_run=command_last_run,
            description=description,
        )

        add_checklist_item_json_body.additional_properties = d
        return add_checklist_item_json_body

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
