from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SamlCertificateStatus")


@attr.s(auto_attribs=True)
class SamlCertificateStatus:
    """
    Attributes:
        idp_certificate_file (Union[Unset, bool]): Status is good when `true`
        public_certificate_file (Union[Unset, bool]): Status is good when `true`
        private_key_file (Union[Unset, bool]): Status is good when `true`
    """

    idp_certificate_file: Union[Unset, bool] = UNSET
    public_certificate_file: Union[Unset, bool] = UNSET
    private_key_file: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idp_certificate_file = self.idp_certificate_file
        public_certificate_file = self.public_certificate_file
        private_key_file = self.private_key_file

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idp_certificate_file is not UNSET:
            field_dict["idp_certificate_file"] = idp_certificate_file
        if public_certificate_file is not UNSET:
            field_dict["public_certificate_file"] = public_certificate_file
        if private_key_file is not UNSET:
            field_dict["private_key_file"] = private_key_file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        idp_certificate_file = d.pop("idp_certificate_file", UNSET)

        public_certificate_file = d.pop("public_certificate_file", UNSET)

        private_key_file = d.pop("private_key_file", UNSET)

        saml_certificate_status = cls(
            idp_certificate_file=idp_certificate_file,
            public_certificate_file=public_certificate_file,
            private_key_file=private_key_file,
        )

        saml_certificate_status.additional_properties = d
        return saml_certificate_status

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
