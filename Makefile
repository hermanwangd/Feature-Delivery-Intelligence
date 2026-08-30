.PHONY: bootstrap validate test score

PYTHON ?= .venv/bin/python

bootstrap:
	python3 -m venv .venv
	.venv/bin/python -m pip install --disable-pip-version-check -r requirements-dev.txt

validate:
	@test -x "$(PYTHON)" || (echo "Run 'make bootstrap' first" >&2; exit 2)
	$(PYTHON) -m unittest discover -s tests -p 'test_*.py' -v

test: validate

score:
	@test -x "$(PYTHON)" || (echo "Run 'make bootstrap' first" >&2; exit 2)
	$(PYTHON) -m validation.scoring.score --cohort validation/features --output validation/scoring/outputs/cohort.json
