.PHONY: new
new:
# https://stackoverflow.com/questions/6273608/how-to-pass-argument-to-makefile-from-command-line/6273809#6273809
	@python3 ./.scripts/touch.py $(filter-out $@,$(MAKECMDGOALS))

%:	# if rule is not found, do nothing, silently
	@:

.PHONY: verify
verify:
	@python3 ./.scripts/genmd.py --verify

.PHONY: regenerate
regenerate:
	@python3 ./.scripts/genmd.py

.PHONY: install
install:
	@python3 setup.py install

.PHONY: test-all
test-all:
	@coverage run -m pytest

.PHONY: test
test:
	@git status --porcelain \
		| awk 'match($$2, "tests/*"){print $$2}' \
		| xargs coverage run -m pytest -vv

.PHONY: coverage
coverage: test-all
	@coverage html
	@coverage xml
	@coverage report

.PHONY: git-add
git-add:
	@git add .
	@pre-commit
	@git add .

.PHONY: add
add: git-add test

.PHONY: commit
commit: add
	@git status --porcelain \
		| awk 'match($$2, "leetcode/*"){print $$2}' \
		| awk '{split($$0, a, "/"); print a[2]}' \
		| sed 's/.py$$//' \
		| sed 's/^p\([0-9]*\)_/\1 - /' \
		| sed 's/_/ /g' > .GIT_COMMIT_MSG

	@git commit -F .GIT_COMMIT_MSG
	@rm .GIT_COMMIT_MSG
