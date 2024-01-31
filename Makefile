.SILENT: install test lint selfcheck check build brain_games

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_code --cov-report xml

package-install:
	 python3 -m pip install --user dist/*.whl

selfcheck:
	poetry check

check: selfcheck test lint

build: chek
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games