from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_graph_book_authors_item import OpenGraphBookAuthorsItem


T = TypeVar("T", bound="OpenGraphBook")


@attr.s(auto_attribs=True)
class OpenGraphBook:
    """Book object used in OpenGraph metadata of a webpage, if type is book

    Attributes:
        isbn (Union[Unset, str]):
        release_date (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        authors (Union[Unset, List['OpenGraphBookAuthorsItem']]):
    """

    isbn: Union[Unset, str] = UNSET
    release_date: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    authors: Union[Unset, List["OpenGraphBookAuthorsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        isbn = self.isbn
        release_date = self.release_date
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        authors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()

                authors.append(authors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if tags is not UNSET:
            field_dict["tags"] = tags
        if authors is not UNSET:
            field_dict["authors"] = authors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_graph_book_authors_item import OpenGraphBookAuthorsItem

        d = src_dict.copy()
        isbn = d.pop("isbn", UNSET)

        release_date = d.pop("release_date", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        authors = []
        _authors = d.pop("authors", UNSET)
        for authors_item_data in _authors or []:
            authors_item = OpenGraphBookAuthorsItem.from_dict(authors_item_data)

            authors.append(authors_item)

        open_graph_book = cls(
            isbn=isbn,
            release_date=release_date,
            tags=tags,
            authors=authors,
        )

        open_graph_book.additional_properties = d
        return open_graph_book

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
