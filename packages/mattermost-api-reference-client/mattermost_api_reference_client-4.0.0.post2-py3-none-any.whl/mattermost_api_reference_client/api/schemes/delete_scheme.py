from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    scheme_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/schemes/{scheme_id}".format(client.base_url, scheme_id=scheme_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
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
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = cast(Any, None)
        return response_501
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
    scheme_id: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Delete a scheme

     Soft deletes a scheme, by marking the scheme as deleted in the database.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        scheme_id=scheme_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scheme_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Delete a scheme

     Soft deletes a scheme, by marking the scheme as deleted in the database.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return sync_detailed(
        scheme_id=scheme_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scheme_id: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Delete a scheme

     Soft deletes a scheme, by marking the scheme as deleted in the database.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        scheme_id=scheme_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scheme_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Delete a scheme

     Soft deletes a scheme, by marking the scheme as deleted in the database.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return (
        await asyncio_detailed(
            scheme_id=scheme_id,
            client=client,
        )
    ).parsed
