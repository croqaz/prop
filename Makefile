.PHONY: test clean update lint coverage

ENV=

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf build
	rm -rf dist
	python3 setup.py clean

update:
	${ENV}pip install -U -r requirements-dev.txt

lint:
	# stop if there are Python syntax errors or undefined names
	${ENV}flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings
	${ENV}flake8 . --count --exit-zero --statistics

coverage:
	${ENV}pytest --cov-report term --cov-report xml --cov=prop/ test/

test:
	${ENV}pytest -ra -sv test/
