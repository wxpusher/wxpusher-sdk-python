.PHONY: clean install lint flake8 pylint test dist upload

PIPENV := $(shell command -v pipenv > /dev/null && echo env)
PIPRUN := $(shell command -v pipenv > /dev/null && echo pipenv run)

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -rf
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	-rm -rf build dist *.egg-info
	-rm -rf .tox .coverage

install:
	pip$(PIPENV) install .

lint: flake8 pylint

flake8:
	${PIPRUN} flake8 setup.py wxpusher

pylint:
	${PIPRUN} pylint setup.py wxpusher

test:
	tox

dist: clean
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
