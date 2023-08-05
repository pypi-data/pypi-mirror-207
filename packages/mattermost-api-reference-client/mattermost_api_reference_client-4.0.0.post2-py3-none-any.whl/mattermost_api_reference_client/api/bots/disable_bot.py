from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.bot import Bot
from ...types import Response


def _get_kwargs(
    bot_user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v4/bots/{bot_user_id}/disable".format(client.base_url, bot_user_id=bot_user_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Bot]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Bot.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Bot]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Bot]]:
    """Disable a bot

     Disable a bot.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Bot]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Bot]]:
    """Disable a bot

     Disable a bot.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Bot]
    """

    return sync_detailed(
        bot_user_id=bot_user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bot_user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Bot]]:
    """Disable a bot

     Disable a bot.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Bot]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Bot]]:
    """Disable a bot

     Disable a bot.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Bot]
    """

    return (
        await asyncio_detailed(
            bot_user_id=bot_user_id,
            client=client,
        )
    ).parsed
