from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Timezone")


@attr.s(auto_attribs=True)
class Timezone:
    """
    Attributes:
        use_automatic_timezone (Union[Unset, bool]): Set to "true" to use the browser/system timezone, "false" to set
            manually. Defaults to "true".
        manual_timezone (Union[Unset, str]): Value when setting manually the timezone, i.e. "Europe/Berlin".
        automatic_timezone (Union[Unset, str]): This value is set automatically when the "useAutomaticTimezone" is set
            to "true".
    """

    use_automatic_timezone: Union[Unset, bool] = UNSET
    manual_timezone: Union[Unset, str] = UNSET
    automatic_timezone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_automatic_timezone = self.use_automatic_timezone
        manual_timezone = self.manual_timezone
        automatic_timezone = self.automatic_timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_automatic_timezone is not UNSET:
            field_dict["useAutomaticTimezone"] = use_automatic_timezone
        if manual_timezone is not UNSET:
            field_dict["manualTimezone"] = manual_timezone
        if automatic_timezone is not UNSET:
            field_dict["automaticTimezone"] = automatic_timezone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        use_automatic_timezone = d.pop("useAutomaticTimezone", UNSET)

        manual_timezone = d.pop("manualTimezone", UNSET)

        automatic_timezone = d.pop("automaticTimezone", UNSET)

        timezone = cls(
            use_automatic_timezone=use_automatic_timezone,
            manual_timezone=manual_timezone,
            automatic_timezone=automatic_timezone,
        )

        timezone.additional_properties = d
        return timezone

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
