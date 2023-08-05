from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.post_list_with_search_matches import PostListWithSearchMatches
from ...models.search_posts_json_body import SearchPostsJsonBody
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/teams/{team_id}/posts/search".format(client.base_url, team_id=team_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, PostListWithSearchMatches]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostListWithSearchMatches.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, PostListWithSearchMatches]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Response[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostListWithSearchMatches]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Optional[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostListWithSearchMatches]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Response[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostListWithSearchMatches]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Optional[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostListWithSearchMatches]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
