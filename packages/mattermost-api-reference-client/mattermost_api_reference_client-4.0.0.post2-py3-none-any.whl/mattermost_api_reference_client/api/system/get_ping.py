from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.system_status_response import SystemStatusResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    get_server_status: Union[Unset, None, bool] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v4/system/ping".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["get_server_status"] = get_server_status

    params["device_id"] = device_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, SystemStatusResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SystemStatusResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, SystemStatusResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    get_server_status: Union[Unset, None, bool] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, SystemStatusResponse]]:
    r"""Check system health

     Check if the server is up and healthy based on the configuration setting `GoRoutineHealthThreshold`.
    If `GoRoutineHealthThreshold` and the number of goroutines on the server exceeds that threshold the
    server is considered unhealthy. If `GoRoutineHealthThreshold` is not set or the number of goroutines
    is below the threshold the server is considered healthy.
    __Minimum server version__: 3.10
    If a \"device_id\" is passed in the query, it will test the Push Notification Proxy in order to
    discover whether the device is able to receive notifications. The response will have a
    \"CanReceiveNotifications\" property with one of the following values: - true: It can receive
    notifications - false: It cannot receive notifications - unknown: There has been an unknown error,
    and it is not certain whether it can
      receive notifications.

    __Minimum server version__: 6.5
    ##### Permissions
    None.

    Args:
        get_server_status (Union[Unset, None, bool]):
        device_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SystemStatusResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        get_server_status=get_server_status,
        device_id=device_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    get_server_status: Union[Unset, None, bool] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, SystemStatusResponse]]:
    r"""Check system health

     Check if the server is up and healthy based on the configuration setting `GoRoutineHealthThreshold`.
    If `GoRoutineHealthThreshold` and the number of goroutines on the server exceeds that threshold the
    server is considered unhealthy. If `GoRoutineHealthThreshold` is not set or the number of goroutines
    is below the threshold the server is considered healthy.
    __Minimum server version__: 3.10
    If a \"device_id\" is passed in the query, it will test the Push Notification Proxy in order to
    discover whether the device is able to receive notifications. The response will have a
    \"CanReceiveNotifications\" property with one of the following values: - true: It can receive
    notifications - false: It cannot receive notifications - unknown: There has been an unknown error,
    and it is not certain whether it can
      receive notifications.

    __Minimum server version__: 6.5
    ##### Permissions
    None.

    Args:
        get_server_status (Union[Unset, None, bool]):
        device_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SystemStatusResponse]
    """

    return sync_detailed(
        client=client,
        get_server_status=get_server_status,
        device_id=device_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    get_server_status: Union[Unset, None, bool] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, SystemStatusResponse]]:
    r"""Check system health

     Check if the server is up and healthy based on the configuration setting `GoRoutineHealthThreshold`.
    If `GoRoutineHealthThreshold` and the number of goroutines on the server exceeds that threshold the
    server is considered unhealthy. If `GoRoutineHealthThreshold` is not set or the number of goroutines
    is below the threshold the server is considered healthy.
    __Minimum server version__: 3.10
    If a \"device_id\" is passed in the query, it will test the Push Notification Proxy in order to
    discover whether the device is able to receive notifications. The response will have a
    \"CanReceiveNotifications\" property with one of the following values: - true: It can receive
    notifications - false: It cannot receive notifications - unknown: There has been an unknown error,
    and it is not certain whether it can
      receive notifications.

    __Minimum server version__: 6.5
    ##### Permissions
    None.

    Args:
        get_server_status (Union[Unset, None, bool]):
        device_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SystemStatusResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        get_server_status=get_server_status,
        device_id=device_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    get_server_status: Union[Unset, None, bool] = UNSET,
    device_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, SystemStatusResponse]]:
    r"""Check system health

     Check if the server is up and healthy based on the configuration setting `GoRoutineHealthThreshold`.
    If `GoRoutineHealthThreshold` and the number of goroutines on the server exceeds that threshold the
    server is considered unhealthy. If `GoRoutineHealthThreshold` is not set or the number of goroutines
    is below the threshold the server is considered healthy.
    __Minimum server version__: 3.10
    If a \"device_id\" is passed in the query, it will test the Push Notification Proxy in order to
    discover whether the device is able to receive notifications. The response will have a
    \"CanReceiveNotifications\" property with one of the following values: - true: It can receive
    notifications - false: It cannot receive notifications - unknown: There has been an unknown error,
    and it is not certain whether it can
      receive notifications.

    __Minimum server version__: 6.5
    ##### Permissions
    None.

    Args:
        get_server_status (Union[Unset, None, bool]):
        device_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SystemStatusResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            get_server_status=get_server_status,
            device_id=device_id,
        )
    ).parsed
