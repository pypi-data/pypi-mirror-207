from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submit_interactive_dialog_json_body_submission import SubmitInteractiveDialogJsonBodySubmission


T = TypeVar("T", bound="SubmitInteractiveDialogJsonBody")


@attr.s(auto_attribs=True)
class SubmitInteractiveDialogJsonBody:
    """
    Attributes:
        url (str): The URL to send the submitted dialog payload to
        channel_id (str): Channel ID the user submitted the dialog from
        team_id (str): Team ID the user submitted the dialog from
        submission (SubmitInteractiveDialogJsonBodySubmission): String map where keys are element names and values are
            the element input values
        callback_id (Union[Unset, str]): Callback ID sent when the dialog was opened
        state (Union[Unset, str]): State sent when the dialog was opened
        cancelled (Union[Unset, bool]): Set to true if the dialog was cancelled
    """

    url: str
    channel_id: str
    team_id: str
    submission: "SubmitInteractiveDialogJsonBodySubmission"
    callback_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    cancelled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        channel_id = self.channel_id
        team_id = self.team_id
        submission = self.submission.to_dict()

        callback_id = self.callback_id
        state = self.state
        cancelled = self.cancelled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "channel_id": channel_id,
                "team_id": team_id,
                "submission": submission,
            }
        )
        if callback_id is not UNSET:
            field_dict["callback_id"] = callback_id
        if state is not UNSET:
            field_dict["state"] = state
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.submit_interactive_dialog_json_body_submission import SubmitInteractiveDialogJsonBodySubmission

        d = src_dict.copy()
        url = d.pop("url")

        channel_id = d.pop("channel_id")

        team_id = d.pop("team_id")

        submission = SubmitInteractiveDialogJsonBodySubmission.from_dict(d.pop("submission"))

        callback_id = d.pop("callback_id", UNSET)

        state = d.pop("state", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        submit_interactive_dialog_json_body = cls(
            url=url,
            channel_id=channel_id,
            team_id=team_id,
            submission=submission,
            callback_id=callback_id,
            state=state,
            cancelled=cancelled,
        )

        submit_interactive_dialog_json_body.additional_properties = d
        return submit_interactive_dialog_json_body

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
