from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.generate_mfa_secret_response_200 import GenerateMfaSecretResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/{user_id}/mfa/generate".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, GenerateMfaSecretResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GenerateMfaSecretResponse200.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, GenerateMfaSecretResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GenerateMfaSecretResponse200]]:
    """Generate MFA secret

     Generates an multi-factor authentication secret for a user and returns it as a string and as base64
    encoded QR code image.
    ##### Permissions
    Must be logged in as the user or have the `edit_other_users` permission.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GenerateMfaSecretResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GenerateMfaSecretResponse200]]:
    """Generate MFA secret

     Generates an multi-factor authentication secret for a user and returns it as a string and as base64
    encoded QR code image.
    ##### Permissions
    Must be logged in as the user or have the `edit_other_users` permission.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GenerateMfaSecretResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GenerateMfaSecretResponse200]]:
    """Generate MFA secret

     Generates an multi-factor authentication secret for a user and returns it as a string and as base64
    encoded QR code image.
    ##### Permissions
    Must be logged in as the user or have the `edit_other_users` permission.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GenerateMfaSecretResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GenerateMfaSecretResponse200]]:
    """Generate MFA secret

     Generates an multi-factor authentication secret for a user and returns it as a string and as base64
    encoded QR code image.
    ##### Permissions
    Must be logged in as the user or have the `edit_other_users` permission.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GenerateMfaSecretResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
