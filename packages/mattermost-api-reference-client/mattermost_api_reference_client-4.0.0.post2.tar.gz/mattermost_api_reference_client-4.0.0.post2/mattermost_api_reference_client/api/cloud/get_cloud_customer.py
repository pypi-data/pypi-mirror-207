from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.cloud_customer import CloudCustomer
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/cloud/customer".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, CloudCustomer]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CloudCustomer.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, CloudCustomer]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, CloudCustomer]]:
    """Get cloud customer

     Retrieves the customer information for the Mattermost Cloud customer bound to this installation.
    ##### Permissions
    Must have `manage_system` permission and be licensed for Cloud.
    __Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to
    change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CloudCustomer]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, CloudCustomer]]:
    """Get cloud customer

     Retrieves the customer information for the Mattermost Cloud customer bound to this installation.
    ##### Permissions
    Must have `manage_system` permission and be licensed for Cloud.
    __Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to
    change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CloudCustomer]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, CloudCustomer]]:
    """Get cloud customer

     Retrieves the customer information for the Mattermost Cloud customer bound to this installation.
    ##### Permissions
    Must have `manage_system` permission and be licensed for Cloud.
    __Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to
    change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CloudCustomer]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, CloudCustomer]]:
    """Get cloud customer

     Retrieves the customer information for the Mattermost Cloud customer bound to this installation.
    ##### Permissions
    Must have `manage_system` permission and be licensed for Cloud.
    __Minimum server version__: 5.28 __Note:__ This is intended for internal use and is subject to
    change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CloudCustomer]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
