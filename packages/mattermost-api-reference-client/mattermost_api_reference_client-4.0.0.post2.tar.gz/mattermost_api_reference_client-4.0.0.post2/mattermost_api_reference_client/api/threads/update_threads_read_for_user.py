from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...types import Response


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/{user_id}/teams/{team_id}/threads/read".format(
        client.base_url, user_id=user_id, team_id=team_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
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
) -> Response[Any]:
    """Mark all threads that user is following as read

     Mark all threads that user is following as read

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Mark all threads that user is following as read

     Mark all threads that user is following as read

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
