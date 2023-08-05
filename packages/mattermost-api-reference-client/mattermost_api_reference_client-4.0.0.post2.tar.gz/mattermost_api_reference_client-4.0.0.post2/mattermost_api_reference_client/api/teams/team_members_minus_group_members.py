from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    group_ids: str = "",
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/api/v4/teams/{team_id}/members_minus_group_members".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["group_ids"] = group_ids

    params["page"] = page

    params["per_page"] = per_page

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
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
    team_id: str,
    *,
    client: Client,
    group_ids: str = "",
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
) -> Response[Any]:
    """Team members minus group members.

     Get the set of users who are members of the team minus the set of users who are members of the given
    groups.
    Each user object contains an array of group objects representing the group memberships for that
    user.
    Each user object contains the boolean fields `scheme_guest`, `scheme_user`, and `scheme_admin`
    representing the roles that user has for the given team.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.14

    Args:
        team_id (str):
        group_ids (str):  Default: ''.
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        group_ids=group_ids,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    group_ids: str = "",
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
) -> Response[Any]:
    """Team members minus group members.

     Get the set of users who are members of the team minus the set of users who are members of the given
    groups.
    Each user object contains an array of group objects representing the group memberships for that
    user.
    Each user object contains the boolean fields `scheme_guest`, `scheme_user`, and `scheme_admin`
    representing the roles that user has for the given team.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.14

    Args:
        team_id (str):
        group_ids (str):  Default: ''.
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        group_ids=group_ids,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
