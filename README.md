# near-omni-client

**near-omni-client** is minimal Python library to interact with the NEAR blockchain and [Chain Signatures].

## Features

- Lightweight
- Fully asynchronous

## Getting Started

Install the latest version of `near-omni-client` by running:

```bash
$ pip install near-omni-client

# or if using uv

$ uv add near-omni-client
```

Create a NEAR account and get your private key using the [NEAR CLI].

## Development quick start

**near-omni-client** uses Python 3.11.11 or higher and uv 0.6.0 or higher.

You can run the following commands in your terminal to check your local Python and uv versions:

```bash
$ python --version

$ uv --version
```

If the versions are not correct or you don't have Python or uv installed, download and follow their setup instructions:

- Python: install with [pyenv]
- uv: follow the official [uv installation instructions]

Once you have these installed, make sure you install the project dependencies by running: 

```bash
$ git clone https://github.com/Omni-rs/near-omni-client.git

$ uv sync
```

<!-- REFERENCES -->

[pyenv]: https://github.com/pyenv/pyenv
[uv installation instructions]: https://github.com/astral-sh/uv?tab=readme-ov-file#installation
[NEAR CLI]: https://github.com/near/near-cli-rs
[Chain Signatures]: https://docs.near.org/chain-abstraction/chain-signatures