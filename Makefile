.PHONY: bootstrap validate test test-functional test-release test-all score

PYTHON ?= .venv/bin/python

bootstrap:
	python3 -m venv .venv
	.venv/bin/python -m pip install --disable-pip-version-check -r requirements-dev.txt

validate:
	@test -x "$(PYTHON)" || (echo "Run 'make bootstrap' first" >&2; exit 2)
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py' -v

test-functional:
	@test -x "$(PYTHON)" || (echo "Run 'make bootstrap' first" >&2; exit 2)
	PYTHONPATH=. PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q --ignore=tests/test_release_guards.py

test-release:
	@test -x "$(PYTHON)" || (echo "Run 'make bootstrap' first" >&2; exit 2)
	PYTHONPATH=. PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m pytest -q tests/test_release_guards.py

test-all: validate test-functional test-release

test: test-all

score:
	@test -x "$(PYTHON)" || (echo "Run 'make bootstrap' first" >&2; exit 2)
	$(PYTHON) -m validation.scoring.score --cohort validation/features --output validation/scoring/outputs/cohort.json
