from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamStats")


@attr.s(auto_attribs=True)
class TeamStats:
    """
    Attributes:
        team_id (Union[Unset, str]):
        total_member_count (Union[Unset, int]):
        active_member_count (Union[Unset, int]):
    """

    team_id: Union[Unset, str] = UNSET
    total_member_count: Union[Unset, int] = UNSET
    active_member_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        total_member_count = self.total_member_count
        active_member_count = self.active_member_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if total_member_count is not UNSET:
            field_dict["total_member_count"] = total_member_count
        if active_member_count is not UNSET:
            field_dict["active_member_count"] = active_member_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("team_id", UNSET)

        total_member_count = d.pop("total_member_count", UNSET)

        active_member_count = d.pop("active_member_count", UNSET)

        team_stats = cls(
            team_id=team_id,
            total_member_count=total_member_count,
            active_member_count=active_member_count,
        )

        team_stats.additional_properties = d
        return team_stats

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
