from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.region_state_now_view_model import RegionStateNowViewModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    zip_: str,
) -> Dict[str, Any]:
    url = "{}/v1/now".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["zip"] = zip_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RegionStateNowViewModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RegionStateNowViewModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RegionStateNowViewModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    zip_: str,
) -> Response[RegionStateNowViewModel]:
    """Returns current RegionState

    Args:
        zip_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegionStateNowViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        zip_=zip_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    zip_: str,
) -> Optional[RegionStateNowViewModel]:
    """Returns current RegionState

    Args:
        zip_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegionStateNowViewModel
    """

    return sync_detailed(
        client=client,
        zip_=zip_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    zip_: str,
) -> Response[RegionStateNowViewModel]:
    """Returns current RegionState

    Args:
        zip_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegionStateNowViewModel]
    """

    kwargs = _get_kwargs(
        client=client,
        zip_=zip_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    zip_: str,
) -> Optional[RegionStateNowViewModel]:
    """Returns current RegionState

    Args:
        zip_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegionStateNowViewModel
    """

    return (
        await asyncio_detailed(
            client=client,
            zip_=zip_,
        )
    ).parsed
