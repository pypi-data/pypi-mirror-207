from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import File, Unset

T = TypeVar("T", bound="ImportTeamMultipartData")


@attr.s(auto_attribs=True)
class ImportTeamMultipartData:
    """
    Attributes:
        file (File): A file to be uploaded in zip format.
        filesize (int): The size of the zip file to be imported.
        import_from (str): String that defines from which application the team was exported to be imported into
            Mattermost.
    """

    file: File
    filesize: int
    import_from: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        filesize = self.filesize
        import_from = self.import_from

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "filesize": filesize,
                "importFrom": import_from,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        filesize = (
            self.filesize if isinstance(self.filesize, Unset) else (None, str(self.filesize).encode(), "text/plain")
        )
        import_from = (
            self.import_from
            if isinstance(self.import_from, Unset)
            else (None, str(self.import_from).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "file": file,
                "filesize": filesize,
                "importFrom": import_from,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        filesize = d.pop("filesize")

        import_from = d.pop("importFrom")

        import_team_multipart_data = cls(
            file=file,
            filesize=filesize,
            import_from=import_from,
        )

        import_team_multipart_data.additional_properties = d
        return import_team_multipart_data

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
