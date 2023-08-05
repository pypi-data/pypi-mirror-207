from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...models.update_user_password_json_body import UpdateUserPasswordJsonBody
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserPasswordJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/{user_id}/password".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StatusOK.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserPasswordJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a user's password

     Update a user's password. New password must meet password policy set by server configuration.
    Current password is required if you're updating your own password.
    ##### Permissions
    Must be logged in as the user the password is being changed for or have `manage_system` permission.

    Args:
        user_id (str):
        json_body (UpdateUserPasswordJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserPasswordJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a user's password

     Update a user's password. New password must meet password policy set by server configuration.
    Current password is required if you're updating your own password.
    ##### Permissions
    Must be logged in as the user the password is being changed for or have `manage_system` permission.

    Args:
        user_id (str):
        json_body (UpdateUserPasswordJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserPasswordJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a user's password

     Update a user's password. New password must meet password policy set by server configuration.
    Current password is required if you're updating your own password.
    ##### Permissions
    Must be logged in as the user the password is being changed for or have `manage_system` permission.

    Args:
        user_id (str):
        json_body (UpdateUserPasswordJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserPasswordJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a user's password

     Update a user's password. New password must meet password policy set by server configuration.
    Current password is required if you're updating your own password.
    ##### Permissions
    Must be logged in as the user the password is being changed for or have `manage_system` permission.

    Args:
        user_id (str):
        json_body (UpdateUserPasswordJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
