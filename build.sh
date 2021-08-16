#!/usr/bin/env bash

set -e
shopt -s globstar

echo "Accessing templates"
cd templates

echo "Run linting"
echo "------------"
for d in * ; do
    echo "cfn-lint" $d
    cfn-lint -t $d
done
