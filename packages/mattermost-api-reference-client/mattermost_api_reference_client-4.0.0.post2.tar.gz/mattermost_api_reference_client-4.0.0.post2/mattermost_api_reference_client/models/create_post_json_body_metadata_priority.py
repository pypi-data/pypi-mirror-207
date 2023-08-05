from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePostJsonBodyMetadataPriority")


@attr.s(auto_attribs=True)
class CreatePostJsonBodyMetadataPriority:
    """An object containing the post's priority properties

    Attributes:
        priority (Union[Unset, str]): The priority label of the post, could empty, important, or urgent
        requested_ack (Union[Unset, bool]): Set to true to request for acknowledgements
    """

    priority: Union[Unset, str] = UNSET
    requested_ack: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        priority = self.priority
        requested_ack = self.requested_ack

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority is not UNSET:
            field_dict["priority"] = priority
        if requested_ack is not UNSET:
            field_dict["requested_ack"] = requested_ack

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        priority = d.pop("priority", UNSET)

        requested_ack = d.pop("requested_ack", UNSET)

        create_post_json_body_metadata_priority = cls(
            priority=priority,
            requested_ack=requested_ack,
        )

        create_post_json_body_metadata_priority.additional_properties = d
        return create_post_json_body_metadata_priority

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
