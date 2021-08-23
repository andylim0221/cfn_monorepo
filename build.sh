#!/usr/bin/env bash

echo "Accessing templates"

cfn-lint templates/**/*.yaml
EXIT_CODE=$?

# Exit code 4 is warnings, which we don't want to error. See https://github.com/aws-cloudformation/cfn-python-lint/issues/235#issuecomment-406951041
if [ $EXIT_CODE == 4 ]; then
  EXIT_CODE=0
fi

exit $EXIT_CODE 