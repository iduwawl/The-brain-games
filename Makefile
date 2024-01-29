#!/usr/bin/env python3

.SILENT: install test build brain-games lint selfcheck check build

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet-code --cov-report xml

publish:
	poetry publish --dry-run

package-install:
	 python3 -m pip install --user dist/*.whl

brain-games:
	poetry run python3 -m brain_games.scripts.brain_games

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build: chek
	poetry build