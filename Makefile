install:
	pip install -U pip
	pip install -e .[tests,docs]

tests:
	pytest -vv --cov=mcache --disable-warnings
