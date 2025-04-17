test:
    uv run pytest

docs:
    sphinx-build docs/source docs/build

docs-clean:
    rm -rf docs/build
