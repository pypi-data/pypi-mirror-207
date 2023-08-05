from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    include_timezones: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/v4/channels/{channel_id}/member_counts_by_group".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["include_timezones"] = include_timezones

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
    channel_id: str,
    *,
    client: Client,
    include_timezones: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Channel members counts for each group that has atleast one member in the channel

     Returns a set of ChannelMemberCountByGroup objects which contain a `group_id`,
    `channel_member_count` and a `channel_member_timezones_count`.
    ##### Permissions
    Must have `read_channel` permission for the given channel.
    __Minimum server version__: 5.24

    Args:
        channel_id (str):
        include_timezones (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        include_timezones=include_timezones,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
    include_timezones: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Channel members counts for each group that has atleast one member in the channel

     Returns a set of ChannelMemberCountByGroup objects which contain a `group_id`,
    `channel_member_count` and a `channel_member_timezones_count`.
    ##### Permissions
    Must have `read_channel` permission for the given channel.
    __Minimum server version__: 5.24

    Args:
        channel_id (str):
        include_timezones (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        include_timezones=include_timezones,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
