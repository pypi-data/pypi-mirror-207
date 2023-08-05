from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_data import JobData


T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """
    Attributes:
        id (Union[Unset, str]): The unique id of the job
        type (Union[Unset, str]): The type of job
        create_at (Union[Unset, int]): The time at which the job was created
        start_at (Union[Unset, int]): The time at which the job was started
        last_activity_at (Union[Unset, int]): The last time at which the job had activity
        status (Union[Unset, str]): The status of the job
        progress (Union[Unset, int]): The progress (as a percentage) of the job
        data (Union[Unset, JobData]): A freeform data field containing additional information about the job
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    create_at: Union[Unset, int] = UNSET
    start_at: Union[Unset, int] = UNSET
    last_activity_at: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    progress: Union[Unset, int] = UNSET
    data: Union[Unset, "JobData"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        create_at = self.create_at
        start_at = self.start_at
        last_activity_at = self.last_activity_at
        status = self.status
        progress = self.progress
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at
        if status is not UNSET:
            field_dict["status"] = status
        if progress is not UNSET:
            field_dict["progress"] = progress
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_data import JobData

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        create_at = d.pop("create_at", UNSET)

        start_at = d.pop("start_at", UNSET)

        last_activity_at = d.pop("last_activity_at", UNSET)

        status = d.pop("status", UNSET)

        progress = d.pop("progress", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, JobData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = JobData.from_dict(_data)

        job = cls(
            id=id,
            type=type,
            create_at=create_at,
            start_at=start_at,
            last_activity_at=last_activity_at,
            status=status,
            progress=progress,
            data=data,
        )

        job.additional_properties = d
        return job

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
