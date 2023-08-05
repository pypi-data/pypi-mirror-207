from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.attach_device_id_json_body import AttachDeviceIdJsonBody
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AttachDeviceIdJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/sessions/device".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
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
    *,
    client: Client,
    json_body: AttachDeviceIdJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Attach mobile device

     Attach a mobile device id to the currently logged in session. This will enable push notifications
    for a user, if configured by the server.
    ##### Permissions
    Must be authenticated.

    Args:
        json_body (AttachDeviceIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: AttachDeviceIdJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Attach mobile device

     Attach a mobile device id to the currently logged in session. This will enable push notifications
    for a user, if configured by the server.
    ##### Permissions
    Must be authenticated.

    Args:
        json_body (AttachDeviceIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AttachDeviceIdJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Attach mobile device

     Attach a mobile device id to the currently logged in session. This will enable push notifications
    for a user, if configured by the server.
    ##### Permissions
    Must be authenticated.

    Args:
        json_body (AttachDeviceIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: AttachDeviceIdJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Attach mobile device

     Attach a mobile device id to the currently logged in session. This will enable push notifications
    for a user, if configured by the server.
    ##### Permissions
    Must be authenticated.

    Args:
        json_body (AttachDeviceIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
