from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePlaybookRunFromDialogJsonBodySubmission")


@attr.s(auto_attribs=True)
class CreatePlaybookRunFromDialogJsonBodySubmission:
    """Map of the dialog fields to their values

    Attributes:
        playbook_id (str): ID of the playbook to create the playbook run from. Example: ahz0s61gh275i7z2ag4g1ntvjm.
        playbook_run_name (str): The name of the playbook run to be created. Example: Server down in EU cluster..
        playbook_run_description (Union[Unset, str]): An optional description of the playbook run. Example: There is one
            server in the EU cluster that is not responding since April 12..
    """

    playbook_id: str
    playbook_run_name: str
    playbook_run_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        playbook_id = self.playbook_id
        playbook_run_name = self.playbook_run_name
        playbook_run_description = self.playbook_run_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playbookID": playbook_id,
                "playbookRunName": playbook_run_name,
            }
        )
        if playbook_run_description is not UNSET:
            field_dict["playbookRunDescription"] = playbook_run_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        playbook_id = d.pop("playbookID")

        playbook_run_name = d.pop("playbookRunName")

        playbook_run_description = d.pop("playbookRunDescription", UNSET)

        create_playbook_run_from_dialog_json_body_submission = cls(
            playbook_id=playbook_id,
            playbook_run_name=playbook_run_name,
            playbook_run_description=playbook_run_description,
        )

        create_playbook_run_from_dialog_json_body_submission.additional_properties = d
        return create_playbook_run_from_dialog_json_body_submission

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
