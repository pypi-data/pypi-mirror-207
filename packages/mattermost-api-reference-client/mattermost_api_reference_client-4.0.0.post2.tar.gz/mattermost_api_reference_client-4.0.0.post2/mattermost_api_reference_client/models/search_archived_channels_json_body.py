from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SearchArchivedChannelsJsonBody")


@attr.s(auto_attribs=True)
class SearchArchivedChannelsJsonBody:
    """
    Attributes:
        term (str): The search term to match against the name or display name of archived channels
    """

    term: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term = self.term

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        term = d.pop("term")

        search_archived_channels_json_body = cls(
            term=term,
        )

        search_archived_channels_json_body.additional_properties = d
        return search_archived_channels_json_body

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
