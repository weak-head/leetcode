.PHONY: new
new:
# https://stackoverflow.com/questions/6273608/how-to-pass-argument-to-makefile-from-command-line/6273809#6273809
	@python3 ./scripts/touch.py $(filter-out $@,$(MAKECMDGOALS))

%:	# if rule is not found, do nothing, silently
	@:

.PHONY: verify
verify:
	@python3 ./scripts/genmd.py --verify

.PHONY: regenerate
regenerate:
	@python3 ./scripts/genmd.py

.PHONY: install
install:
	@python3 setup.py install

.PHONY: test
test:
	@coverage run -m pytest

.PHONY: coverage
coverage: test
	@coverage html
	@coverage report

.PHONY: git-add
git-add:
	@git add .
	@pre-commit
	@git add .

.PHONY: add
add: git-add test