.PHONY: build-env install install-pkg install-dev test clean reset publish bump-major bump-minor bump-patch

PACKAGE = lv_velodyne

activate-env := . env/bin/activate

build-env:
	python -m venv env
	$(call activate-env) && python -m pip install --upgrade pip flit bump2version;

install: install-pkg install-dev

install-pkg:
	$(call activate-env) && flit install --deps production --symlink;

install-dev:
	$(call activate-env) && flit install --deps develop --symlink;

test:
	$(call activate-env) && pytest -vv -s tests;

publish:
	$(call activate-env) && flit publish;

bump-major:
	bump2version major

bump-minor:
	bump2version minor

bump-patch:
	bump2version patch

lint-check:
	$(call activate-env) && black --check $(PACKAGE)/ tests/;
	$(call activate-env) && isort --check $(PACKAGE)/ tests/;

lint:
	$(call activate-env) && black $(PACKAGE)/ tests/;
	$(call activate-env) && isort $(PACKAGE)/ tests/;

clean:
	rm -rf env
	rm -rf build
	rm -rf dist
	rm -rf $(PACKAGE).egg-info
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

reset: clean build-env install
