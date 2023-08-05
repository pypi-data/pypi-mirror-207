from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupSyncableChannel")


@attr.s(auto_attribs=True)
class GroupSyncableChannel:
    """
    Attributes:
        channel_id (Union[Unset, str]):
        group_id (Union[Unset, str]):
        auto_add (Union[Unset, bool]):
        create_at (Union[Unset, int]):
        delete_at (Union[Unset, int]):
        update_at (Union[Unset, int]):
    """

    channel_id: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    auto_add: Union[Unset, bool] = UNSET
    create_at: Union[Unset, int] = UNSET
    delete_at: Union[Unset, int] = UNSET
    update_at: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id
        group_id = self.group_id
        auto_add = self.auto_add
        create_at = self.create_at
        delete_at = self.delete_at
        update_at = self.update_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if auto_add is not UNSET:
            field_dict["auto_add"] = auto_add
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if delete_at is not UNSET:
            field_dict["delete_at"] = delete_at
        if update_at is not UNSET:
            field_dict["update_at"] = update_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id", UNSET)

        group_id = d.pop("group_id", UNSET)

        auto_add = d.pop("auto_add", UNSET)

        create_at = d.pop("create_at", UNSET)

        delete_at = d.pop("delete_at", UNSET)

        update_at = d.pop("update_at", UNSET)

        group_syncable_channel = cls(
            channel_id=channel_id,
            group_id=group_id,
            auto_add=auto_add,
            create_at=create_at,
            delete_at=delete_at,
            update_at=update_at,
        )

        group_syncable_channel.additional_properties = d
        return group_syncable_channel

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
