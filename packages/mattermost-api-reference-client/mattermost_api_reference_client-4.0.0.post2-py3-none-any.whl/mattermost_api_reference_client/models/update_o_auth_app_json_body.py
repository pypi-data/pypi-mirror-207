from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateOAuthAppJsonBody")


@attr.s(auto_attribs=True)
class UpdateOAuthAppJsonBody:
    """
    Attributes:
        id (str): The id of the client application
        name (str): The name of the client application
        description (str): A short description of the application
        callback_urls (List[str]): A list of callback URLs for the appliation
        homepage (str): A link to the website of the application
        icon_url (Union[Unset, str]): A URL to an icon to display with the application
        is_trusted (Union[Unset, bool]): Set this to `true` to skip asking users for permission. It will be set to false
            if value is not provided.
    """

    id: str
    name: str
    description: str
    callback_urls: List[str]
    homepage: str
    icon_url: Union[Unset, str] = UNSET
    is_trusted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        callback_urls = self.callback_urls

        homepage = self.homepage
        icon_url = self.icon_url
        is_trusted = self.is_trusted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "callback_urls": callback_urls,
                "homepage": homepage,
            }
        )
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if is_trusted is not UNSET:
            field_dict["is_trusted"] = is_trusted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        callback_urls = cast(List[str], d.pop("callback_urls"))

        homepage = d.pop("homepage")

        icon_url = d.pop("icon_url", UNSET)

        is_trusted = d.pop("is_trusted", UNSET)

        update_o_auth_app_json_body = cls(
            id=id,
            name=name,
            description=description,
            callback_urls=callback_urls,
            homepage=homepage,
            icon_url=icon_url,
            is_trusted=is_trusted,
        )

        update_o_auth_app_json_body.additional_properties = d
        return update_o_auth_app_json_body

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
