 lam.PHONY: help install test docs-serve

help:
	@echo "-----------------------"
	@echo "Available make targets:"
	@echo ""
	@echo "help	 	- show this help"
	@echo "install		- install all dependencies"
	@echo "test  		- run all tests"
	@echo "docs-serve	- run the documentation server"
	@echo "-----------------------"

install:
	uv sync

test:
	uv run pytest

docs-serve:
	uv run mkdocs serve

.DEFAULT_GOAL := help