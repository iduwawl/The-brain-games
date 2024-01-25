#!/usr/bin/env python3

.SILENT: install build publish package-install brain-games

setup: install build publish package-install

install: # установить зависимости
	poetry install

build: # собрать проект
	poetry build

publish: # опубликовать
	poetry publish --dry-run

package-install: # установить в окружение пользователя
	 python3 -m pip install --user dist/*.whl

brain-games: # запустить
	poetry run python3 -m brain_games.scripts.brain_games


