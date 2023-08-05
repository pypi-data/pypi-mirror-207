from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.upgrade_to_enterprise_status_response_200 import UpgradeToEnterpriseStatusResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/upgrade_to_enterprise/status".format(client.base_url)

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, UpgradeToEnterpriseStatusResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpgradeToEnterpriseStatusResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, UpgradeToEnterpriseStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, UpgradeToEnterpriseStatusResponse200]]:
    """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition

     It returns the percentage of completion of the current upgrade or the error if there is any.
    __Minimum server version__: 5.27
    ##### Permissions
    Must have `manage_system` permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpgradeToEnterpriseStatusResponse200]]
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
) -> Optional[Union[Any, UpgradeToEnterpriseStatusResponse200]]:
    """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition

     It returns the percentage of completion of the current upgrade or the error if there is any.
    __Minimum server version__: 5.27
    ##### Permissions
    Must have `manage_system` permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpgradeToEnterpriseStatusResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, UpgradeToEnterpriseStatusResponse200]]:
    """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition

     It returns the percentage of completion of the current upgrade or the error if there is any.
    __Minimum server version__: 5.27
    ##### Permissions
    Must have `manage_system` permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpgradeToEnterpriseStatusResponse200]]
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
) -> Optional[Union[Any, UpgradeToEnterpriseStatusResponse200]]:
    """Get the current status for the inplace upgrade from Team Edition to Enterprise Edition

     It returns the percentage of completion of the current upgrade or the error if there is any.
    __Minimum server version__: 5.27
    ##### Permissions
    Must have `manage_system` permission.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpgradeToEnterpriseStatusResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
