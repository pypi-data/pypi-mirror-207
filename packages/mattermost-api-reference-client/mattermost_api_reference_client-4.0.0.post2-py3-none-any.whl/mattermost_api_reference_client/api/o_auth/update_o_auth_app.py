from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.o_auth_app import OAuthApp
from ...models.update_o_auth_app_json_body import UpdateOAuthAppJsonBody
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    client: Client,
    json_body: UpdateOAuthAppJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/oauth/apps/{app_id}".format(client.base_url, app_id=app_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, OAuthApp]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OAuthApp.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, OAuthApp]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: Client,
    json_body: UpdateOAuthAppJsonBody,
) -> Response[Union[Any, OAuthApp]]:
    """Update an OAuth app

     Update an OAuth 2.0 client application based on OAuth struct.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):
        json_body (UpdateOAuthAppJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuthApp]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: Client,
    json_body: UpdateOAuthAppJsonBody,
) -> Optional[Union[Any, OAuthApp]]:
    """Update an OAuth app

     Update an OAuth 2.0 client application based on OAuth struct.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):
        json_body (UpdateOAuthAppJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OAuthApp]
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: Client,
    json_body: UpdateOAuthAppJsonBody,
) -> Response[Union[Any, OAuthApp]]:
    """Update an OAuth app

     Update an OAuth 2.0 client application based on OAuth struct.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):
        json_body (UpdateOAuthAppJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuthApp]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: Client,
    json_body: UpdateOAuthAppJsonBody,
) -> Optional[Union[Any, OAuthApp]]:
    """Update an OAuth app

     Update an OAuth 2.0 client application based on OAuth struct.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):
        json_body (UpdateOAuthAppJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OAuthApp]
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
