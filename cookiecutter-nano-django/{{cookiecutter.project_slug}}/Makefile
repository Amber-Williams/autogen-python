SHELL = /bin/bash
.SHELLFLAGS = -o pipefail -c

.PHONY: install
install: ## installs dependencies
	poetry install
	poetry run pre-commit install

.PHONY: start
start: ## starts the app
	poetry run start

.PHONY: test
test: ## runs tests
	poetry run test

.PHONY: dustoff
dustoff: ## formats and verifies code
	poetry run format && poetry run lint

