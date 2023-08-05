from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwitchAccountTypeJsonBody")


@attr.s(auto_attribs=True)
class SwitchAccountTypeJsonBody:
    """
    Attributes:
        current_service (str): The service the user currently uses to login
        new_service (str): The service the user will use to login
        email (Union[Unset, str]): The email of the user
        password (Union[Unset, str]): The password used with the current service
        mfa_code (Union[Unset, str]): The MFA code of the current service
        ldap_id (Union[Unset, str]): The LDAP/AD id of the user
    """

    current_service: str
    new_service: str
    email: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    mfa_code: Union[Unset, str] = UNSET
    ldap_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_service = self.current_service
        new_service = self.new_service
        email = self.email
        password = self.password
        mfa_code = self.mfa_code
        ldap_id = self.ldap_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_service": current_service,
                "new_service": new_service,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if mfa_code is not UNSET:
            field_dict["mfa_code"] = mfa_code
        if ldap_id is not UNSET:
            field_dict["ldap_id"] = ldap_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_service = d.pop("current_service")

        new_service = d.pop("new_service")

        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        mfa_code = d.pop("mfa_code", UNSET)

        ldap_id = d.pop("ldap_id", UNSET)

        switch_account_type_json_body = cls(
            current_service=current_service,
            new_service=new_service,
            email=email,
            password=password,
            mfa_code=mfa_code,
            ldap_id=ldap_id,
        )

        switch_account_type_json_body.additional_properties = d
        return switch_account_type_json_body

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
