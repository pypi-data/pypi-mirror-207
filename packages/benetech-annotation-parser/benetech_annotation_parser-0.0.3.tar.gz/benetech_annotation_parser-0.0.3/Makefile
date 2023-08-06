quality:
	black src tests
	autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables src tests
	isort src tests
	pflake8 src tests

check:
	black --check src tests
    isort --check-only src tests
    pflake8 src tests