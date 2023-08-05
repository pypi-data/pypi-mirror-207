from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.create_post_json_body import CreatePostJsonBody
from ...models.post import Post
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: CreatePostJsonBody,
    set_online: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v4/posts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["set_online"] = set_online

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Post]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Post.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Post]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreatePostJsonBody,
    set_online: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Post]]:
    """Create a post

     Create a new post in a channel. To create the post as a comment on another post, provide `root_id`.
    ##### Permissions
    Must have `create_post` permission for the channel the post is being created in.

    Args:
        set_online (Union[Unset, None, bool]):
        json_body (CreatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        set_online=set_online,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CreatePostJsonBody,
    set_online: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Post]]:
    """Create a post

     Create a new post in a channel. To create the post as a comment on another post, provide `root_id`.
    ##### Permissions
    Must have `create_post` permission for the channel the post is being created in.

    Args:
        set_online (Union[Unset, None, bool]):
        json_body (CreatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Post]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        set_online=set_online,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreatePostJsonBody,
    set_online: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Post]]:
    """Create a post

     Create a new post in a channel. To create the post as a comment on another post, provide `root_id`.
    ##### Permissions
    Must have `create_post` permission for the channel the post is being created in.

    Args:
        set_online (Union[Unset, None, bool]):
        json_body (CreatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        set_online=set_online,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreatePostJsonBody,
    set_online: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Post]]:
    """Create a post

     Create a new post in a channel. To create the post as a comment on another post, provide `root_id`.
    ##### Permissions
    Must have `create_post` permission for the channel the post is being created in.

    Args:
        set_online (Union[Unset, None, bool]):
        json_body (CreatePostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Post]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            set_online=set_online,
        )
    ).parsed
