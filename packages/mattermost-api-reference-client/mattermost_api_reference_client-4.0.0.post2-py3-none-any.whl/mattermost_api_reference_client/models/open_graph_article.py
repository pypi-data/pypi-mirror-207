from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_graph_article_authors_item import OpenGraphArticleAuthorsItem


T = TypeVar("T", bound="OpenGraphArticle")


@attr.s(auto_attribs=True)
class OpenGraphArticle:
    """Article object used in OpenGraph metadata of a webpage, if type is article

    Attributes:
        published_time (Union[Unset, str]):
        modified_time (Union[Unset, str]):
        expiration_time (Union[Unset, str]):
        section (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        authors (Union[Unset, List['OpenGraphArticleAuthorsItem']]):
    """

    published_time: Union[Unset, str] = UNSET
    modified_time: Union[Unset, str] = UNSET
    expiration_time: Union[Unset, str] = UNSET
    section: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    authors: Union[Unset, List["OpenGraphArticleAuthorsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        published_time = self.published_time
        modified_time = self.modified_time
        expiration_time = self.expiration_time
        section = self.section
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
        if published_time is not UNSET:
            field_dict["published_time"] = published_time
        if modified_time is not UNSET:
            field_dict["modified_time"] = modified_time
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if section is not UNSET:
            field_dict["section"] = section
        if tags is not UNSET:
            field_dict["tags"] = tags
        if authors is not UNSET:
            field_dict["authors"] = authors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_graph_article_authors_item import OpenGraphArticleAuthorsItem

        d = src_dict.copy()
        published_time = d.pop("published_time", UNSET)

        modified_time = d.pop("modified_time", UNSET)

        expiration_time = d.pop("expiration_time", UNSET)

        section = d.pop("section", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        authors = []
        _authors = d.pop("authors", UNSET)
        for authors_item_data in _authors or []:
            authors_item = OpenGraphArticleAuthorsItem.from_dict(authors_item_data)

            authors.append(authors_item)

        open_graph_article = cls(
            published_time=published_time,
            modified_time=modified_time,
            expiration_time=expiration_time,
            section=section,
            tags=tags,
            authors=authors,
        )

        open_graph_article.additional_properties = d
        return open_graph_article

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
