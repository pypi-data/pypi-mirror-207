from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.app_error import AppError
from ...models.user_terms_of_service import UserTermsOfService
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/{user_id}/terms_of_service".format(client.base_url, user_id=user_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, AppError, UserTermsOfService]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserTermsOfService.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = AppError.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, AppError, UserTermsOfService]]:
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
) -> Response[Union[Any, AppError, UserTermsOfService]]:
    """Fetches user's latest terms of service action if the latest action was for acceptance.

     Will be deprecated in v6.0
    Fetches user's latest terms of service action if the latest action was for acceptance.

    __Minimum server version__: 5.6
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppError, UserTermsOfService]]
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
) -> Optional[Union[Any, AppError, UserTermsOfService]]:
    """Fetches user's latest terms of service action if the latest action was for acceptance.

     Will be deprecated in v6.0
    Fetches user's latest terms of service action if the latest action was for acceptance.

    __Minimum server version__: 5.6
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppError, UserTermsOfService]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, AppError, UserTermsOfService]]:
    """Fetches user's latest terms of service action if the latest action was for acceptance.

     Will be deprecated in v6.0
    Fetches user's latest terms of service action if the latest action was for acceptance.

    __Minimum server version__: 5.6
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppError, UserTermsOfService]]
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
) -> Optional[Union[Any, AppError, UserTermsOfService]]:
    """Fetches user's latest terms of service action if the latest action was for acceptance.

     Will be deprecated in v6.0
    Fetches user's latest terms of service action if the latest action was for acceptance.

    __Minimum server version__: 5.6
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppError, UserTermsOfService]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
