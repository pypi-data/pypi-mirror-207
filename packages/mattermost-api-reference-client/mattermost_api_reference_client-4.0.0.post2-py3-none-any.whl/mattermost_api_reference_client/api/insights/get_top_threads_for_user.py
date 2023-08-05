from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.top_thread_list import TopThreadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/me/top/threads".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["time_range"] = time_range

    params["page"] = page

    params["per_page"] = per_page

    params["team_id"] = team_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, TopThreadList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TopThreadList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, TopThreadList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, TopThreadList]]:
    """Get a list of the top threads for a user.

     Get a list of the top threads from public and private channels (the user is a member of and
    participating in the thread) for a given user.
    ##### Permissions
    Must be logged in as the user.

    Args:
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TopThreadList]]
    """

    kwargs = _get_kwargs(
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
        team_id=team_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, TopThreadList]]:
    """Get a list of the top threads for a user.

     Get a list of the top threads from public and private channels (the user is a member of and
    participating in the thread) for a given user.
    ##### Permissions
    Must be logged in as the user.

    Args:
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TopThreadList]
    """

    return sync_detailed(
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
        team_id=team_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, TopThreadList]]:
    """Get a list of the top threads for a user.

     Get a list of the top threads from public and private channels (the user is a member of and
    participating in the thread) for a given user.
    ##### Permissions
    Must be logged in as the user.

    Args:
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TopThreadList]]
    """

    kwargs = _get_kwargs(
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
        team_id=team_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, TopThreadList]]:
    """Get a list of the top threads for a user.

     Get a list of the top threads from public and private channels (the user is a member of and
    participating in the thread) for a given user.
    ##### Permissions
    Must be logged in as the user.

    Args:
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TopThreadList]
    """

    return (
        await asyncio_detailed(
            client=client,
            time_range=time_range,
            page=page,
            per_page=per_page,
            team_id=team_id,
        )
    ).parsed
