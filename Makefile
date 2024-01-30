

.SILENT: brain-even brain-calc brain-gcd brain-progression brain-prime

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

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime