from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.command import Command
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/teams/{team_id}/commands/autocomplete".format(client.base_url, team_id=team_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, List["Command"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Command.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, List["Command"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List["Command"]]]:
    """List autocomplete commands

     List autocomplete commands in the team.
    ##### Permissions
    `view_team` for the team.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Command']]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List["Command"]]]:
    """List autocomplete commands

     List autocomplete commands in the team.
    ##### Permissions
    `view_team` for the team.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Command']]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List["Command"]]]:
    """List autocomplete commands

     List autocomplete commands in the team.
    ##### Permissions
    `view_team` for the team.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Command']]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List["Command"]]]:
    """List autocomplete commands

     List autocomplete commands in the team.
    ##### Permissions
    `view_team` for the team.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Command']]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
        )
    ).parsed
