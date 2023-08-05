from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checklist import Checklist


T = TypeVar("T", bound="Playbook")


@attr.s(auto_attribs=True)
class Playbook:
    """
    Attributes:
        id (Union[Unset, str]): A unique, 26 characters long, alphanumeric identifier for the playbook. Example:
            iz0g457ikesz55dhxcfa0fk9yy.
        title (Union[Unset, str]): The title of the playbook. Example: Cloud PlaybookRuns.
        description (Union[Unset, str]): The description of the playbook. Example: A playbook to follow when there is a
            playbook run regarding the availability of the cloud service..
        team_id (Union[Unset, str]): The identifier of the team where the playbook is in. Example:
            p03rbi6viyztysbqnkvcqyel2i.
        create_public_playbook_run (Union[Unset, bool]): A boolean indicating whether the playbook runs created from
            this playbook should be public or private. Example: True.
        create_at (Union[Unset, int]): The playbook creation timestamp, formatted as the number of milliseconds since
            the Unix epoch. Example: 1602235338837.
        delete_at (Union[Unset, int]): The playbook deletion timestamp, formatted as the number of milliseconds since
            the Unix epoch. It equals 0 if the playbook is not deleted.
        num_stages (Union[Unset, int]): The number of stages defined in this playbook. Example: 3.
        num_steps (Union[Unset, int]): The total number of steps from all the stages defined in this playbook. Example:
            18.
        checklists (Union[Unset, List['Checklist']]): The stages defined in this playbook.
        member_ids (Union[Unset, List[str]]): The identifiers of all the users that are members of this playbook.
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    create_public_playbook_run: Union[Unset, bool] = UNSET
    create_at: Union[Unset, int] = UNSET
    delete_at: Union[Unset, int] = UNSET
    num_stages: Union[Unset, int] = UNSET
    num_steps: Union[Unset, int] = UNSET
    checklists: Union[Unset, List["Checklist"]] = UNSET
    member_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        description = self.description
        team_id = self.team_id
        create_public_playbook_run = self.create_public_playbook_run
        create_at = self.create_at
        delete_at = self.delete_at
        num_stages = self.num_stages
        num_steps = self.num_steps
        checklists: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.checklists, Unset):
            checklists = []
            for checklists_item_data in self.checklists:
                checklists_item = checklists_item_data.to_dict()

                checklists.append(checklists_item)

        member_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.member_ids, Unset):
            member_ids = self.member_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if create_public_playbook_run is not UNSET:
            field_dict["create_public_playbook_run"] = create_public_playbook_run
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if delete_at is not UNSET:
            field_dict["delete_at"] = delete_at
        if num_stages is not UNSET:
            field_dict["num_stages"] = num_stages
        if num_steps is not UNSET:
            field_dict["num_steps"] = num_steps
        if checklists is not UNSET:
            field_dict["checklists"] = checklists
        if member_ids is not UNSET:
            field_dict["member_ids"] = member_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checklist import Checklist

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        team_id = d.pop("team_id", UNSET)

        create_public_playbook_run = d.pop("create_public_playbook_run", UNSET)

        create_at = d.pop("create_at", UNSET)

        delete_at = d.pop("delete_at", UNSET)

        num_stages = d.pop("num_stages", UNSET)

        num_steps = d.pop("num_steps", UNSET)

        checklists = []
        _checklists = d.pop("checklists", UNSET)
        for checklists_item_data in _checklists or []:
            checklists_item = Checklist.from_dict(checklists_item_data)

            checklists.append(checklists_item)

        member_ids = cast(List[str], d.pop("member_ids", UNSET))

        playbook = cls(
            id=id,
            title=title,
            description=description,
            team_id=team_id,
            create_public_playbook_run=create_public_playbook_run,
            create_at=create_at,
            delete_at=delete_at,
            num_stages=num_stages,
            num_steps=num_steps,
            checklists=checklists,
            member_ids=member_ids,
        )

        playbook.additional_properties = d
        return playbook

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
