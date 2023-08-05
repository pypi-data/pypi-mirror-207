from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.create_user_access_token_json_body import CreateUserAccessTokenJsonBody
from ...models.user_access_token import UserAccessToken
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: CreateUserAccessTokenJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/{user_id}/tokens".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, UserAccessToken]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UserAccessToken.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, UserAccessToken]]:
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
    json_body: CreateUserAccessTokenJsonBody,
) -> Response[Union[Any, UserAccessToken]]:
    """Create a user access token

     Generate a user access token that can be used to authenticate with the Mattermost REST API.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (CreateUserAccessTokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserAccessToken]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
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
    json_body: CreateUserAccessTokenJsonBody,
) -> Optional[Union[Any, UserAccessToken]]:
    """Create a user access token

     Generate a user access token that can be used to authenticate with the Mattermost REST API.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (CreateUserAccessTokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserAccessToken]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: CreateUserAccessTokenJsonBody,
) -> Response[Union[Any, UserAccessToken]]:
    """Create a user access token

     Generate a user access token that can be used to authenticate with the Mattermost REST API.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (CreateUserAccessTokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserAccessToken]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    json_body: CreateUserAccessTokenJsonBody,
) -> Optional[Union[Any, UserAccessToken]]:
    """Create a user access token

     Generate a user access token that can be used to authenticate with the Mattermost REST API.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (CreateUserAccessTokenJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserAccessToken]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
