from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.user_autocomplete import UserAutocomplete
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    name: str,
    limit: Union[Unset, None, int] = 100,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/autocomplete".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["team_id"] = team_id

    params["channel_id"] = channel_id

    params["name"] = name

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, UserAutocomplete]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserAutocomplete.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, UserAutocomplete]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    name: str,
    limit: Union[Unset, None, int] = 100,
) -> Response[Union[Any, UserAutocomplete]]:
    """Autocomplete users

     Get a list of users for the purpose of autocompleting based on the provided search term. Specify a
    combination of `team_id` and `channel_id` to filter results further.
    ##### Permissions
    Requires an active session and `view_team` and `read_channel` on any teams or channels used to
    filter the results further.

    Args:
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        name (str):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserAutocomplete]]
    """

    kwargs = _get_kwargs(
        client=client,
        team_id=team_id,
        channel_id=channel_id,
        name=name,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    name: str,
    limit: Union[Unset, None, int] = 100,
) -> Optional[Union[Any, UserAutocomplete]]:
    """Autocomplete users

     Get a list of users for the purpose of autocompleting based on the provided search term. Specify a
    combination of `team_id` and `channel_id` to filter results further.
    ##### Permissions
    Requires an active session and `view_team` and `read_channel` on any teams or channels used to
    filter the results further.

    Args:
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        name (str):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserAutocomplete]
    """

    return sync_detailed(
        client=client,
        team_id=team_id,
        channel_id=channel_id,
        name=name,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    name: str,
    limit: Union[Unset, None, int] = 100,
) -> Response[Union[Any, UserAutocomplete]]:
    """Autocomplete users

     Get a list of users for the purpose of autocompleting based on the provided search term. Specify a
    combination of `team_id` and `channel_id` to filter results further.
    ##### Permissions
    Requires an active session and `view_team` and `read_channel` on any teams or channels used to
    filter the results further.

    Args:
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        name (str):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserAutocomplete]]
    """

    kwargs = _get_kwargs(
        client=client,
        team_id=team_id,
        channel_id=channel_id,
        name=name,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    name: str,
    limit: Union[Unset, None, int] = 100,
) -> Optional[Union[Any, UserAutocomplete]]:
    """Autocomplete users

     Get a list of users for the purpose of autocompleting based on the provided search term. Specify a
    combination of `team_id` and `channel_id` to filter results further.
    ##### Permissions
    Requires an active session and `view_team` and `read_channel` on any teams or channels used to
    filter the results further.

    Args:
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        name (str):
        limit (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserAutocomplete]
    """

    return (
        await asyncio_detailed(
            client=client,
            team_id=team_id,
            channel_id=channel_id,
            name=name,
            limit=limit,
        )
    ).parsed
