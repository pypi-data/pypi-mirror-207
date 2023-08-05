from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendWarnMetricAckJsonBody")


@attr.s(auto_attribs=True)
class SendWarnMetricAckJsonBody:
    """
    Attributes:
        force_ack (Union[Unset, bool]): Flag which determines if the ack for the metric warning should be directly
            stored (without trying to send email first) or not
    """

    force_ack: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        force_ack = self.force_ack

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force_ack is not UNSET:
            field_dict["forceAck"] = force_ack

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        force_ack = d.pop("forceAck", UNSET)

        send_warn_metric_ack_json_body = cls(
            force_ack=force_ack,
        )

        send_warn_metric_ack_json_body.additional_properties = d
        return send_warn_metric_ack_json_body

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
