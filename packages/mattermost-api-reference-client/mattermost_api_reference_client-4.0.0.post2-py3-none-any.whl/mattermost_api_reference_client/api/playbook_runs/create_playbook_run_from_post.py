from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_playbook_run_from_post_json_body import CreatePlaybookRunFromPostJsonBody
from ...models.playbook_run import PlaybookRun
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CreatePlaybookRunFromPostJsonBody,
) -> Dict[str, Any]:
    url = "{}/plugins/playbooks/api/v0/runs".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, PlaybookRun]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = PlaybookRun.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, PlaybookRun]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreatePlaybookRunFromPostJsonBody,
) -> Response[Union[Any, PlaybookRun]]:
    """Create a new playbook run

     Create a new playbook run in a team, using a playbook as template, with a specific name and a
    specific owner.

    Args:
        json_body (CreatePlaybookRunFromPostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaybookRun]]
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
    client: AuthenticatedClient,
    json_body: CreatePlaybookRunFromPostJsonBody,
) -> Optional[Union[Any, PlaybookRun]]:
    """Create a new playbook run

     Create a new playbook run in a team, using a playbook as template, with a specific name and a
    specific owner.

    Args:
        json_body (CreatePlaybookRunFromPostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaybookRun]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreatePlaybookRunFromPostJsonBody,
) -> Response[Union[Any, PlaybookRun]]:
    """Create a new playbook run

     Create a new playbook run in a team, using a playbook as template, with a specific name and a
    specific owner.

    Args:
        json_body (CreatePlaybookRunFromPostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaybookRun]]
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
    client: AuthenticatedClient,
    json_body: CreatePlaybookRunFromPostJsonBody,
) -> Optional[Union[Any, PlaybookRun]]:
    """Create a new playbook run

     Create a new playbook run in a team, using a playbook as template, with a specific name and a
    specific owner.

    Args:
        json_body (CreatePlaybookRunFromPostJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaybookRun]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
