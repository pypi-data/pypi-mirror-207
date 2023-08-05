from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

import attr

from ..types import File

T = TypeVar("T", bound="UploadSamlPrivateCertificateMultipartData")


@attr.s(auto_attribs=True)
class UploadSamlPrivateCertificateMultipartData:
    """
    Attributes:
        certificate (File): The private key file
    """

    certificate: File
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate = self.certificate.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certificate": certificate,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        certificate = self.certificate.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "certificate": certificate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate = File(payload=BytesIO(d.pop("certificate")))

        upload_saml_private_certificate_multipart_data = cls(
            certificate=certificate,
        )

        upload_saml_private_certificate_multipart_data.additional_properties = d
        return upload_saml_private_certificate_multipart_data

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
