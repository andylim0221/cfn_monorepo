#!/usr/bin/env bash

set -e
echo "Accessing templates"

cfn-lint templates/**/*.yaml
EXIT_CODE=$?

if [$EXIT_CODE == 4]; then 
    EXIT_CODE=0
fi 

exit $EXIT_CODE
