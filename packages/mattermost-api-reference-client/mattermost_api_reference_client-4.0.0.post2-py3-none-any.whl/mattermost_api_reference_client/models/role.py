from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Role")


@attr.s(auto_attribs=True)
class Role:
    """
    Attributes:
        id (Union[Unset, str]): The unique identifier of the role.
        name (Union[Unset, str]): The unique name of the role, used when assigning roles to users/groups in contexts.
        display_name (Union[Unset, str]): The human readable name for the role.
        description (Union[Unset, str]): A human readable description of the role.
        permissions (Union[Unset, List[str]]): A list of the unique names of the permissions this role grants.
        scheme_managed (Union[Unset, bool]): indicates if this role is managed by a scheme (true), or is a custom stand-
            alone role (false).
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[str]] = UNSET
    scheme_managed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        description = self.description
        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        scheme_managed = self.scheme_managed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if scheme_managed is not UNSET:
            field_dict["scheme_managed"] = scheme_managed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("display_name", UNSET)

        description = d.pop("description", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        scheme_managed = d.pop("scheme_managed", UNSET)

        role = cls(
            id=id,
            name=name,
            display_name=display_name,
            description=description,
            permissions=permissions,
            scheme_managed=scheme_managed,
        )

        role.additional_properties = d
        return role

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
