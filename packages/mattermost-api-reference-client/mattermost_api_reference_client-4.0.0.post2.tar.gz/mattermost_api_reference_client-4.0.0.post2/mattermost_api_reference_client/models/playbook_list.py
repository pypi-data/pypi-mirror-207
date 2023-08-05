from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playbook import Playbook


T = TypeVar("T", bound="PlaybookList")


@attr.s(auto_attribs=True)
class PlaybookList:
    """
    Attributes:
        total_count (Union[Unset, int]): The total number of playbooks in the list, regardless of the paging. Example:
            305.
        page_count (Union[Unset, int]): The total number of pages. This depends on the total number of playbooks in the
            database and the per_page parameter sent with the request. Example: 2.
        has_more (Union[Unset, bool]): A boolean describing whether there are more pages after the currently returned.
            Example: True.
        items (Union[Unset, List['Playbook']]): The playbooks in this page.
    """

    total_count: Union[Unset, int] = UNSET
    page_count: Union[Unset, int] = UNSET
    has_more: Union[Unset, bool] = UNSET
    items: Union[Unset, List["Playbook"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        page_count = self.page_count
        has_more = self.has_more
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.playbook import Playbook

        d = src_dict.copy()
        total_count = d.pop("total_count", UNSET)

        page_count = d.pop("page_count", UNSET)

        has_more = d.pop("has_more", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Playbook.from_dict(items_item_data)

            items.append(items_item)

        playbook_list = cls(
            total_count=total_count,
            page_count=page_count,
            has_more=has_more,
            items=items,
        )

        playbook_list.additional_properties = d
        return playbook_list

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
