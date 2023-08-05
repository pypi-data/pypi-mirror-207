from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.sidebar_category import SidebarCategory
from ...types import Response


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: List["SidebarCategory"],
) -> Dict[str, Any]:
    url = "{}/api/v4/users/{user_id}/teams/{team_id}/channels/categories".format(
        client.base_url, user_id=user_id, team_id=team_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, SidebarCategory]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SidebarCategory.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, SidebarCategory]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: List["SidebarCategory"],
) -> Response[Union[Any, SidebarCategory]]:
    """Update user's sidebar categories

     Update any number of sidebar categories for the user on the given team. This can be used to reorder
    the channels in these categories.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be authenticated and have the `list_team_channels` permission.

    Args:
        user_id (str):
        team_id (str):
        json_body (List['SidebarCategory']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SidebarCategory]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
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
    team_id: str,
    *,
    client: Client,
    json_body: List["SidebarCategory"],
) -> Optional[Union[Any, SidebarCategory]]:
    """Update user's sidebar categories

     Update any number of sidebar categories for the user on the given team. This can be used to reorder
    the channels in these categories.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be authenticated and have the `list_team_channels` permission.

    Args:
        user_id (str):
        team_id (str):
        json_body (List['SidebarCategory']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SidebarCategory]
    """

    return sync_detailed(
        user_id=user_id,
        team_id=team_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: List["SidebarCategory"],
) -> Response[Union[Any, SidebarCategory]]:
    """Update user's sidebar categories

     Update any number of sidebar categories for the user on the given team. This can be used to reorder
    the channels in these categories.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be authenticated and have the `list_team_channels` permission.

    Args:
        user_id (str):
        team_id (str):
        json_body (List['SidebarCategory']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SidebarCategory]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: List["SidebarCategory"],
) -> Optional[Union[Any, SidebarCategory]]:
    """Update user's sidebar categories

     Update any number of sidebar categories for the user on the given team. This can be used to reorder
    the channels in these categories.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be authenticated and have the `list_team_channels` permission.

    Args:
        user_id (str):
        team_id (str):
        json_body (List['SidebarCategory']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SidebarCategory]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
