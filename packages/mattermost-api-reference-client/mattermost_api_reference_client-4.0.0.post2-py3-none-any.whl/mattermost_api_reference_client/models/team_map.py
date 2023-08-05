from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team import Team


T = TypeVar("T", bound="TeamMap")


@attr.s(auto_attribs=True)
class TeamMap:
    """A mapping of teamIds to teams.

    Attributes:
        team_id (Union[Unset, Team]):
    """

    team_id: Union[Unset, "Team"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team_id, Unset):
            team_id = self.team_id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["team_id"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team import Team

        d = src_dict.copy()
        _team_id = d.pop("team_id", UNSET)
        team_id: Union[Unset, Team]
        if isinstance(_team_id, Unset):
            team_id = UNSET
        else:
            team_id = Team.from_dict(_team_id)

        team_map = cls(
            team_id=team_id,
        )

        team_map.additional_properties = d
        return team_map

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
