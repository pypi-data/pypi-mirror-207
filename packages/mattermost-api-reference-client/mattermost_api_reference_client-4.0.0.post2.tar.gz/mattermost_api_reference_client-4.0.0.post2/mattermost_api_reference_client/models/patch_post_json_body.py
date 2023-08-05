from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchPostJsonBody")


@attr.s(auto_attribs=True)
class PatchPostJsonBody:
    """
    Attributes:
        is_pinned (Union[Unset, bool]): Set to `true` to pin the post to the channel it is in
        message (Union[Unset, str]): The message text of the post
        file_ids (Union[Unset, List[str]]): The list of files attached to this post
        has_reactions (Union[Unset, bool]): Set to `true` if the post has reactions to it
        props (Union[Unset, str]): A general JSON property bag to attach to the post
    """

    is_pinned: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    file_ids: Union[Unset, List[str]] = UNSET
    has_reactions: Union[Unset, bool] = UNSET
    props: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_pinned = self.is_pinned
        message = self.message
        file_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        has_reactions = self.has_reactions
        props = self.props

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned
        if message is not UNSET:
            field_dict["message"] = message
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if has_reactions is not UNSET:
            field_dict["has_reactions"] = has_reactions
        if props is not UNSET:
            field_dict["props"] = props

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_pinned = d.pop("is_pinned", UNSET)

        message = d.pop("message", UNSET)

        file_ids = cast(List[str], d.pop("file_ids", UNSET))

        has_reactions = d.pop("has_reactions", UNSET)

        props = d.pop("props", UNSET)

        patch_post_json_body = cls(
            is_pinned=is_pinned,
            message=message,
            file_ids=file_ids,
            has_reactions=has_reactions,
            props=props,
        )

        patch_post_json_body.additional_properties = d
        return patch_post_json_body

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
