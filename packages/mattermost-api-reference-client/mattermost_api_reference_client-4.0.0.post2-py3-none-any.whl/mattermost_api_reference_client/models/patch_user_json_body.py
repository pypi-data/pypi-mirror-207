from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_user_json_body_props import PatchUserJsonBodyProps
    from ..models.user_notify_props import UserNotifyProps


T = TypeVar("T", bound="PatchUserJsonBody")


@attr.s(auto_attribs=True)
class PatchUserJsonBody:
    """
    Attributes:
        email (Union[Unset, str]):
        username (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        nickname (Union[Unset, str]):
        locale (Union[Unset, str]):
        position (Union[Unset, str]):
        props (Union[Unset, PatchUserJsonBodyProps]):
        notify_props (Union[Unset, UserNotifyProps]):
    """

    email: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    props: Union[Unset, "PatchUserJsonBodyProps"] = UNSET
    notify_props: Union[Unset, "UserNotifyProps"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        nickname = self.nickname
        locale = self.locale
        position = self.position
        props: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        notify_props: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notify_props, Unset):
            notify_props = self.notify_props.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if locale is not UNSET:
            field_dict["locale"] = locale
        if position is not UNSET:
            field_dict["position"] = position
        if props is not UNSET:
            field_dict["props"] = props
        if notify_props is not UNSET:
            field_dict["notify_props"] = notify_props

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_user_json_body_props import PatchUserJsonBodyProps
        from ..models.user_notify_props import UserNotifyProps

        d = src_dict.copy()
        email = d.pop("email", UNSET)

        username = d.pop("username", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        nickname = d.pop("nickname", UNSET)

        locale = d.pop("locale", UNSET)

        position = d.pop("position", UNSET)

        _props = d.pop("props", UNSET)
        props: Union[Unset, PatchUserJsonBodyProps]
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = PatchUserJsonBodyProps.from_dict(_props)

        _notify_props = d.pop("notify_props", UNSET)
        notify_props: Union[Unset, UserNotifyProps]
        if isinstance(_notify_props, Unset):
            notify_props = UNSET
        else:
            notify_props = UserNotifyProps.from_dict(_notify_props)

        patch_user_json_body = cls(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            locale=locale,
            position=position,
            props=props,
            notify_props=notify_props,
        )

        patch_user_json_body.additional_properties = d
        return patch_user_json_body

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
