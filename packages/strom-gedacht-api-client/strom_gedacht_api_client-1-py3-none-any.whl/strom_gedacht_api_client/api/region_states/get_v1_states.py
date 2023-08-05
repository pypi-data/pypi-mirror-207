import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.region_state_range_view_model import RegionStateRangeViewModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    zip_: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Dict[str, Any]:
    url = "{}/v1/states".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["zip"] = zip_

    json_from_ = from_.isoformat()

    params["from"] = json_from_

    json_to = to.isoformat()

    params["to"] = json_to

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, RegionStateRangeViewModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RegionStateRangeViewModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, RegionStateRangeViewModel]]:
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
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[Union[Any, RegionStateRangeViewModel]]:
    """Returns requested region states

    Args:
        zip_ (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegionStateRangeViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        zip_=zip_,
        from_=from_,
        to=to,
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
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Optional[Union[Any, RegionStateRangeViewModel]]:
    """Returns requested region states

    Args:
        zip_ (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RegionStateRangeViewModel]
    """

    return sync_detailed(
        client=client,
        zip_=zip_,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    zip_: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[Union[Any, RegionStateRangeViewModel]]:
    """Returns requested region states

    Args:
        zip_ (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegionStateRangeViewModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        zip_=zip_,
        from_=from_,
        to=to,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    zip_: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Optional[Union[Any, RegionStateRangeViewModel]]:
    """Returns requested region states

    Args:
        zip_ (str):
        from_ (datetime.datetime):
        to (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RegionStateRangeViewModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            zip_=zip_,
            from_=from_,
            to=to,
        )
    ).parsed
