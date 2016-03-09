.PHONY: all deps lint format test
SHELL := /bin/bash

all: format lint test

deps:
	python setup.py develop

format:
	autopep8 -i -r -j0 -a --experimental --max-line-length 100 --indent-size 2 .

lint:
	pep8 --config ./pep8 . || true

test: deps
	nosetests ./test
