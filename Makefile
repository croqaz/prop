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
	${ENV}flake8 --count --statistics

coverage:
	${ENV}pytest --cov-report term --cov=dot test/

test:
	${ENV}pytest -rasv test/
