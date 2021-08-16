#!/usr/bin/env bash

set -e
shopt -s globstar

cfn-lint templates/**/*.yaml
