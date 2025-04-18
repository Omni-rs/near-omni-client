test:
    uv run pytest

docs:
    sphinx-build docs/source docs/build

docs-clean:
    rm -rf docs/build

docs-serve: docs
    cd docs/build && python3 -m http.server 8000 & open http://localhost:8000

lint:
    uv run ruff check .

lint-fix:
	uv run ruff check . --fix

format:
    uv run ruff format .

format-check:
	uv run ruff format . --check

