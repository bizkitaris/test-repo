.PHONY: install test lint clean build

install:
	pip install -e .

test:
	pytest tests/ -v

lint:
	python -m py_compile src/hello_possum/*.py

clean:
	rm -rf build/ dist/ *.egg-info __pycache__ .pytest_cache

build: clean
	python -m build
