#!/usr/bin/env python3

.SILENT: install build publish package-install brain-games

setup: install build publish package-install

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


