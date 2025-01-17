POETRY := $(shell command -v poetry 2> /dev/null)

sources = bacalhau_sdk

.`.PHONY: all
all: format lint pre-commit test

.PHONY: test
test: unittest coverage

.PHONY: format
format:
	$(POETRY) run isort $(sources) tests examples
	$(POETRY) run black $(sources) tests examples

.PHONY: lint
lint:
	$(POETRY) run flake8 $(sources) tests examples
	$(POETRY) run mypy $(sources) tests examples

.PHONY: unittest
unittest:
	$(POETRY) run pytest --capture=no --log-cli-level=DEBUG

.PHONY: coverage
coverage:
	$(POETRY) run pytest --cov=$(sources) --cov-branch --cov-report=term-missing tests

.PHONY: install-pre-commit
install-pre-commit:
	$(POETRY) run pre-commit install
	@echo "Pre-commit installed."

.PHONY: pre-commit
pre-commit:
	$(POETRY) run pre-commit run --files ./**/*

.PHONY: clean
clean:
	rm -rf .mypy_cache .pytest_cache
	rm -rf *.egg-info
	rm -rf .tox dist site
	rm -rf coverage.xml .coverage
