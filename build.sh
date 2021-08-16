#!/usr/bin/env bash

set -e
shopt -s extglob

cfn-lint templates/**/*.yaml
