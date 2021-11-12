#!/bin/bash

python -m unittest discover -s tests -p 'test*.py'
result=$?

coverage run -m unittest discover -s tests -p 'test*.py'
coverage report --show-missing --fail-under=60
coverage html --directory=coverage.report

pylint --max-line-length=120 ckunlock/*.py
flake8 --max-line-length=120 ckunlock/*.py

exit $result

