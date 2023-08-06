# WEAO

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Python API wrapper for the <https://whatexploitsare.online> API

## Installation

**Python 3.11 or higher is required**

Install The PyPi Version:

```sh
py -3 -m pip install -U weao
```

You may also install the development version:

```sh
pip install git+https://github.com/xFGhoul/WEAO.git
```

## Usage

Quick Example:

```py
import asyncio

from weao import Client

client = Client()


async def get_exploit():
    exploit = await client.get_exploit("Synapse")
    print(exploit.status)


loop = asyncio.new_event_loop()
loop.run_until_complete(get_exploit())
```

You can find more examples in the [examples](https://github.com/xFGhoul/WEAO/blob/dev/examples/) directory.

## Files and Explanations

`├──`[`.github`](https://github.com/xFGhoul/WEAO/blob/dev/.github) — GitHub configuration including CI/CD workflows<br>
`├──`[`docs`](https://github.com/xFGhoul/WEAO/blob/dev/docs) — Developer Documentation<br>
`├──`[`tests`](https://github.com/xFGhoul/WEAO/blob/dev/tests) — Tests<br>
`├──`[`examples`](https://github.com/xFGhoul/WEAO/blob/dev/examples) — Examples Showing How To Use The Wrapper<br>
`├──`[`weao`](https://github.com/xFGhoul/WEAO/blob/dev/pyprotector) — Source Code Of WEAO<br>

> Made With ❤️ By `ghoul#9497`
