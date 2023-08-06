import aiohttp
import pytest

from weao.client import Client

@pytest.mark.asyncio
async def test_get_exploit() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    exploit = await client.get_exploit("Synapse")
    await client.cleanup()

    assert exploit.website == "https://x.synapse.to"

@pytest.mark.asyncio
async def test_get_status() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    status = await client.get_status()
    await client.cleanup()

    assert status.synapse.website == "https://x.synapse.to"

@pytest.mark.asyncio
async def test_get_logs() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    logs = await client.get_logs("Synapse", 3)
    await client.cleanup()

    assert logs[1].version == "v2.23.9b"