from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalDataRetentionPolicy")


@attr.s(auto_attribs=True)
class GlobalDataRetentionPolicy:
    """
    Attributes:
        message_deletion_enabled (Union[Unset, bool]): Indicates whether data retention policy deletion of messages is
            enabled globally.
        file_deletion_enabled (Union[Unset, bool]): Indicates whether data retention policy deletion of file attachments
            is enabled globally.
        message_retention_cutoff (Union[Unset, int]): The current server timestamp before which messages should be
            deleted.
        file_retention_cutoff (Union[Unset, int]): The current server timestamp before which files should be deleted.
    """

    message_deletion_enabled: Union[Unset, bool] = UNSET
    file_deletion_enabled: Union[Unset, bool] = UNSET
    message_retention_cutoff: Union[Unset, int] = UNSET
    file_retention_cutoff: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message_deletion_enabled = self.message_deletion_enabled
        file_deletion_enabled = self.file_deletion_enabled
        message_retention_cutoff = self.message_retention_cutoff
        file_retention_cutoff = self.file_retention_cutoff

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_deletion_enabled is not UNSET:
            field_dict["message_deletion_enabled"] = message_deletion_enabled
        if file_deletion_enabled is not UNSET:
            field_dict["file_deletion_enabled"] = file_deletion_enabled
        if message_retention_cutoff is not UNSET:
            field_dict["message_retention_cutoff"] = message_retention_cutoff
        if file_retention_cutoff is not UNSET:
            field_dict["file_retention_cutoff"] = file_retention_cutoff

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message_deletion_enabled = d.pop("message_deletion_enabled", UNSET)

        file_deletion_enabled = d.pop("file_deletion_enabled", UNSET)

        message_retention_cutoff = d.pop("message_retention_cutoff", UNSET)

        file_retention_cutoff = d.pop("file_retention_cutoff", UNSET)

        global_data_retention_policy = cls(
            message_deletion_enabled=message_deletion_enabled,
            file_deletion_enabled=file_deletion_enabled,
            message_retention_cutoff=message_retention_cutoff,
            file_retention_cutoff=file_retention_cutoff,
        )

        global_data_retention_policy.additional_properties = d
        return global_data_retention_policy

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
