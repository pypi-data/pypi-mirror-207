from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...models.verify_user_email_json_body import VerifyUserEmailJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: VerifyUserEmailJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/users/email/verify".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StatusOK.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: VerifyUserEmailJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Verify user email

     Verify the email used by a user to sign-up their account with.
    ##### Permissions
    No permissions required.

    Args:
        json_body (VerifyUserEmailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: VerifyUserEmailJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Verify user email

     Verify the email used by a user to sign-up their account with.
    ##### Permissions
    No permissions required.

    Args:
        json_body (VerifyUserEmailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: VerifyUserEmailJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Verify user email

     Verify the email used by a user to sign-up their account with.
    ##### Permissions
    No permissions required.

    Args:
        json_body (VerifyUserEmailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: VerifyUserEmailJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Verify user email

     Verify the email used by a user to sign-up their account with.
    ##### Permissions
    No permissions required.

    Args:
        json_body (VerifyUserEmailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
