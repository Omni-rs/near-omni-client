setup-dev:
	uv sync --all-extras --dev
	uv pip install -e .

test:
    uv run pytest

docs:
    sphinx-build docs/source docs/build

docs-clean:
    rm -rf docs/build

docs-serve: docs
    sphinx-autobuild docs/source docs/_build/html --open-browser

lint:
    uv run ruff check .

lint-fix:
	uv run ruff check . --fix

format:
    uv run ruff format .

format-check:
	uv run ruff format . --check

