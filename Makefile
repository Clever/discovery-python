.PHONY: all clean deps format lint publish test
SHELL := /bin/bash

all: format lint test

clean:
	find -type f -name '*.pyc' -delete

deps:
	python setup.py develop

format:
	autopep8 -i -r -j0 -a --experimental --max-line-length 100 --indent-size 2 .

lint:
	pep8 --config ./pep8 . || true

publish:
	./publish.sh

test: deps
	nosetests ./test
