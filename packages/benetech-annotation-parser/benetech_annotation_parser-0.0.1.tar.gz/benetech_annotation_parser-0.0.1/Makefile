quality:
	black src tests
	autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables src tests
	isort src tests
	flake8 src tests

check:
	black src