.SILENT: brain_games brain-even brain-gcd brain-calc brain-progression brain-prime

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install dist/*.whl --force-reinstall
	
package-uninstall:
	python3 -m pip uninstall -y hexlet-code

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

setup: install build package-install