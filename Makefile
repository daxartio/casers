.DEFAULT_GOAL := help
CODE = casers tests benches
UV_RUN = uv run
TEST = $(UV_RUN) pytest $(args)

.PHONY: help
help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: format lint test  ## Run format lint test

.PHONY: install-uv
install-uv:  ## Install uv
	pip install uv

.PHONY: install
install:  ## Install dependencies
	uv sync --extra pydantic

.PHONY: publish
publish:  ## Publish package
	@$(UV_RUN) maturin upload

.PHONY: build-rs
build-rs:  ## Build .so files
	$(UV_RUN) maturin develop

.PHONY: format-rs
format-rs:  ## Formatting Rust code
	cargo fmt

.PHONY: lint-rs
lint-rs:  ## Check Rust code
	cargo check

.PHONY: test
test:  ## Test with coverage
	$(TEST) --ignore=benches --cov=./

.PHONY: test-fast
test-fast:  ## Test until error
	$(TEST) --exitfirst

.PHONY: test-failed
test-failed:  ## Test failed
	$(TEST) --last-failed

.PHONY: lint
lint:  ## Check code
	$(UV_RUN) ruff check $(CODE)
	$(UV_RUN) ruff format --check $(CODE)
	$(UV_RUN) pytest --dead-fixtures --dup-fixtures
	$(UV_RUN) mypy $(CODE)

.PHONY: format
format:  ## Formatting code
	$(UV_RUN) ruff format $(CODE)

.PHONY: bump
bump:  ## Bump version (commit and tag)
	$(UV_RUN) cz bump --major-version-zero

.PHONY: clean
clean:  ## Clean
	rm -rf site || true
	rm -rf dist || true
	rm -rf htmlcov || true

.PHONY: benchmark
benchmark:  ## Benchmark
	$(TEST) benches/test_to_camel.py

.PHONY: benchmark-all
benchmark-all:  ## Benchmark all
	$(TEST) benches
