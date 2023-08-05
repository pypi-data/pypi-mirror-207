from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...models.upload_ldap_private_certificate_multipart_data import UploadLdapPrivateCertificateMultipartData
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: UploadLdapPrivateCertificateMultipartData,
) -> Dict[str, Any]:
    url = "{}/api/v4/ldap/certificate/private".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StatusOK.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = cast(Any, None)
        return response_501
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
    multipart_data: UploadLdapPrivateCertificateMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Upload private key

     Upload the private key to be used for TLS verification. The server will pick a hard-coded filename
    for the PrivateKeyFile setting in your `config.json`.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        multipart_data (UploadLdapPrivateCertificateMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    multipart_data: UploadLdapPrivateCertificateMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Upload private key

     Upload the private key to be used for TLS verification. The server will pick a hard-coded filename
    for the PrivateKeyFile setting in your `config.json`.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        multipart_data (UploadLdapPrivateCertificateMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: UploadLdapPrivateCertificateMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Upload private key

     Upload the private key to be used for TLS verification. The server will pick a hard-coded filename
    for the PrivateKeyFile setting in your `config.json`.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        multipart_data (UploadLdapPrivateCertificateMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: UploadLdapPrivateCertificateMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Upload private key

     Upload the private key to be used for TLS verification. The server will pick a hard-coded filename
    for the PrivateKeyFile setting in your `config.json`.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        multipart_data (UploadLdapPrivateCertificateMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StatusOK]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
