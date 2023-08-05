from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmCustomerPaymentMultipartData")


@attr.s(auto_attribs=True)
class ConfirmCustomerPaymentMultipartData:
    """
    Attributes:
        stripe_setup_intent_id (Union[Unset, str]):
    """

    stripe_setup_intent_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stripe_setup_intent_id = self.stripe_setup_intent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stripe_setup_intent_id is not UNSET:
            field_dict["stripe_setup_intent_id"] = stripe_setup_intent_id

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        stripe_setup_intent_id = (
            self.stripe_setup_intent_id
            if isinstance(self.stripe_setup_intent_id, Unset)
            else (None, str(self.stripe_setup_intent_id).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if stripe_setup_intent_id is not UNSET:
            field_dict["stripe_setup_intent_id"] = stripe_setup_intent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stripe_setup_intent_id = d.pop("stripe_setup_intent_id", UNSET)

        confirm_customer_payment_multipart_data = cls(
            stripe_setup_intent_id=stripe_setup_intent_id,
        )

        confirm_customer_payment_multipart_data.additional_properties = d
        return confirm_customer_payment_multipart_data

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
