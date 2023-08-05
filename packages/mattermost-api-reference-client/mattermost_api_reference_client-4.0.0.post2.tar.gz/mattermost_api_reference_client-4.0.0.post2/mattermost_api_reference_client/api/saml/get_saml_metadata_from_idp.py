from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_saml_metadata_from_idp_json_body import GetSamlMetadataFromIdpJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v4/saml/metadatafromidp".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Response[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
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
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Optional[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Response[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
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
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Optional[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
