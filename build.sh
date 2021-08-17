#!/usr/bin/env bash

set -e

echo "Accessing templates"
cd templates

c=""
for d in * ; do
    if [[ $d == *.yaml ]]
    then
        c+="$d "
    fi
done

cfn-lint -t $c