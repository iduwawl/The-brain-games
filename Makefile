#!/usr/bin/env python3

.SILENT: brain-games

install: # установить зависимости
	poetry install

build: # собрать проект
	poetry build

publishh: # опубликовать
	poetry publish --dry-run

package-install: # установить в окружение пользователя
	 python3 -m pip install --user dist/*.whl

brain-games: # запустить
	poetry run brain-games


