from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetChecklistAutocompleteResponse200Item")


@attr.s(auto_attribs=True)
class GetChecklistAutocompleteResponse200Item:
    """
    Attributes:
        item (str): A string containing a pair of integers separated by a space. The first integer is the index of the
            checklist; the second is the index of the item within the checklist. Example: 1 2.
        hint (str): The title of the corresponding item. Example: Gather information from customer..
        helptext (str): Always the value "Check/uncheck this item". Example: Check/uncheck this item.
    """

    item: str
    hint: str
    helptext: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item = self.item
        hint = self.hint
        helptext = self.helptext

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item": item,
                "hint": hint,
                "helptext": helptext,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item = d.pop("item")

        hint = d.pop("hint")

        helptext = d.pop("helptext")

        get_checklist_autocomplete_response_200_item = cls(
            item=item,
            hint=hint,
            helptext=helptext,
        )

        get_checklist_autocomplete_response_200_item.additional_properties = d
        return get_checklist_autocomplete_response_200_item

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
