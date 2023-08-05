from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.post import Post
from ...models.update_post_json_body import UpdatePostJsonBody
from ...types import Response


def _get_kwargs(
    post_id: str,
    *,
    client: Client,
    json_body: UpdatePostJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/posts/{post_id}".format(client.base_url, post_id=post_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Post]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Post.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Post]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    post_id: str,
    *,
    client: Client,
    json_body: UpdatePostJsonBody,
) -> Response[Union[Any, Post]]:
    """Update a post

     Update a post. Only the fields listed below are updatable, omitted fields will be treated as blank.
    ##### Permissions
    Must have `edit_post` permission for the channel the post is in.

    Args:
        post_id (str):
        json_body (UpdatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    post_id: str,
    *,
    client: Client,
    json_body: UpdatePostJsonBody,
) -> Optional[Union[Any, Post]]:
    """Update a post

     Update a post. Only the fields listed below are updatable, omitted fields will be treated as blank.
    ##### Permissions
    Must have `edit_post` permission for the channel the post is in.

    Args:
        post_id (str):
        json_body (UpdatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Post]
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: Client,
    json_body: UpdatePostJsonBody,
) -> Response[Union[Any, Post]]:
    """Update a post

     Update a post. Only the fields listed below are updatable, omitted fields will be treated as blank.
    ##### Permissions
    Must have `edit_post` permission for the channel the post is in.

    Args:
        post_id (str):
        json_body (UpdatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    *,
    client: Client,
    json_body: UpdatePostJsonBody,
) -> Optional[Union[Any, Post]]:
    """Update a post

     Update a post. Only the fields listed below are updatable, omitted fields will be treated as blank.
    ##### Permissions
    Must have `edit_post` permission for the channel the post is in.

    Args:
        post_id (str):
        json_body (UpdatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Post]
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
