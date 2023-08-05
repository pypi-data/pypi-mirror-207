from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.command import Command
from ...types import Response


def _get_kwargs(
    command_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/commands/{command_id}".format(client.base_url, command_id=command_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Command]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Command.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Command]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    command_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Command]]:
    """Get a command

     Get a command definition based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    __Minimum server version__: 5.22

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Command]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    command_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Command]]:
    """Get a command

     Get a command definition based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    __Minimum server version__: 5.22

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Command]
    """

    return sync_detailed(
        command_id=command_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    command_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Command]]:
    """Get a command

     Get a command definition based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    __Minimum server version__: 5.22

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Command]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    command_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Command]]:
    """Get a command

     Get a command definition based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    __Minimum server version__: 5.22

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Command]
    """

    return (
        await asyncio_detailed(
            command_id=command_id,
            client=client,
        )
    ).parsed
