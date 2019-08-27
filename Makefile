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

.PHONY: install_dependencies
install_dependencies:
	@pip3 install -r requirements.txt

.PHONY: install
install:
	@python3 setup.py install

.PHONY: test
test: install
	@coverage run -m pytest

.PHONY: coverage
coverage: test
	@coverage html
	@coverage report
