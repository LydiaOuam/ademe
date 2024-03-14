install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black -l 100 **/*.py

lint:
	pylint --disable=R,C,W0105 src/*.py

precommit: format lint
