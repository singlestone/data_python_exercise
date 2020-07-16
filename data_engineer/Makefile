all: unit integration lint requirements.txt requirements-dev.txt

Pipfile.lock: Pipfile
	pipenv lock

.PHONY: requirements.txt
requirements.txt: Pipfile.lock
	pipenv clean
	LLVM_CONFIG=$(shell which llvm-config-7) pipenv sync
	pipenv run pip freeze > requirements.txt

.PHONY: requirements-dev.txt
requirements-dev.txt: Pipfile.lock
	pipenv clean
	LLVM_CONFIG=$(shell which llvm-config-7) pipenv sync --dev
	pipenv run pip freeze > requirements-dev.txt

.PHONY: integration
integration:
	pipenv run python3 -m solution | tee .integration_output
	cat .integration_output | grep 'Steffen Cochern' | grep 'Tracey Scoyles' | grep '52-0676084' && echo integration test passed

.PHONY: unit
unit: requirements-dev.txt
	pipenv run python3 -m unittest

.PHONY: lint
lint: requirements-dev.txt
	pipenv run pylint solution
