from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    logs_per_page: Union[Unset, None, str] = "10000",
) -> Dict[str, Any]:
    url = "{}/api/v4/logs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["logs_per_page"] = logs_per_page

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, List[str]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[str], response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, List[str]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    logs_per_page: Union[Unset, None, str] = "10000",
) -> Response[Union[Any, List[str]]]:
    """Get logs

     Get a page of server logs, selected with `page` and `logs_per_page` query parameters.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        page (Union[Unset, None, int]):
        logs_per_page (Union[Unset, None, str]):  Default: '10000'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[str]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        logs_per_page=logs_per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    logs_per_page: Union[Unset, None, str] = "10000",
) -> Optional[Union[Any, List[str]]]:
    """Get logs

     Get a page of server logs, selected with `page` and `logs_per_page` query parameters.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        page (Union[Unset, None, int]):
        logs_per_page (Union[Unset, None, str]):  Default: '10000'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List[str]]
    """

    return sync_detailed(
        client=client,
        page=page,
        logs_per_page=logs_per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    logs_per_page: Union[Unset, None, str] = "10000",
) -> Response[Union[Any, List[str]]]:
    """Get logs

     Get a page of server logs, selected with `page` and `logs_per_page` query parameters.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        page (Union[Unset, None, int]):
        logs_per_page (Union[Unset, None, str]):  Default: '10000'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[str]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        logs_per_page=logs_per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    logs_per_page: Union[Unset, None, str] = "10000",
) -> Optional[Union[Any, List[str]]]:
    """Get logs

     Get a page of server logs, selected with `page` and `logs_per_page` query parameters.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        page (Union[Unset, None, int]):
        logs_per_page (Union[Unset, None, str]):  Default: '10000'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List[str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            logs_per_page=logs_per_page,
        )
    ).parsed
