#!/usr/bin/env bash

set -e
shopt -s globstar

cd templates
for d in * ; do
    echo "cfn-lint" $d
    cfn-lint -t $d
done
