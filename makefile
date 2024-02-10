.PHONY: check-all
check-all: lint typecheck

.PHONY: lint
lint:
	poetry run ruff .

.PHONY: typecheck
typecheck:
	poetry run mypy .

.PHONY: run
test:
	poetry run python suraburomaji/main.py
