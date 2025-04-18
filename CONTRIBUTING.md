# Development Guide

This guide covers setup and development for **near-omni-client**.

## Contents

- [Development Setup](#development-setup)
- [Testing](#testing)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Changelog](#changelog)

## Development Setup

**near-omni-client** uses Python 3.11.11 or higher, uv 0.6.0 or higher and just.

You can run the following commands in your terminal to check if you have installed the pre requisites.

```bash
$ python --version

$ uv --version

$ just --version
```

If the versions are not correct or you don't have Python, uv or just installed, download and follow their setup instructions:

- Python: install with [pyenv]
- uv: follow the official [uv installation instructions]
- just: follow the official [just installation instructions]

Once you have these installed, make sure you install the project dependencies by running: 

```bash
$ git clone https://github.com/Omni-rs/near-omni-client.git

$ just setup-dev
```

## Testing

All the code should be tested, althought having a 100% coverage is difficult, we aim to have a 80% coverage. 

In order to run the tests run the following command:

```bash
just test
```

## Code Style

We use ruff for linting and formatting.

The following commands are available:

```bash

# format code
$ just format

# check format
$ just format-check

# lint code
$ just lint

# fix linting issue
$ just lint-fix
```

## Documentation

The majority of the documentation is maintained in the [docs] directory and generated using [Sphinx], based on inline Python docstrings and Markdown / ReStructuredText files.

When adding new functionality or modifying existing behavior, please update:

- The relevant docstrings in the codebase.

- Any corresponding `.md` or `.rst` files in [docs] that describe the behavior.

These updates will be reflected automatically in the next documentation build.

<!-- REFERENCES -->

[pyenv]: https://github.com/pyenv/pyenv
[uv installation instructions]: https://github.com/astral-sh/uv?tab=readme-ov-file#installation
[just installation instructions]: https://github.com/casey/just?tab=readme-ov-file#packages
[NEAR CLI]: https://github.com/near/near-cli-rs
[docs]: ./docs
[Sphinx]: https://www.sphinx-doc.org/en/master/