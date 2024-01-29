#!/usr/bin/env python3

.SILENT: install build publish package-install brain-games lint

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	 python3 -m pip install --user dist/*.whl

brain-games:
	poetry run python3 -m brain_games.scripts.brain_games

lint:
	poetry run flake8 brain_games
