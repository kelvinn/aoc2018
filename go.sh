#!/usr/bin/env bash

set -e

run_unit_tests()
{
    python -m unittest discover tests
}

run_lint()
{
    flake8
}

all() {
  run_lint
  run_unit_tests
}

print_usage()
{
cat <<EOF

    Usage: $0 [option]

    lint                (deprecated) run lint checks.
    unit                run unit tests.
    all                 run everything
EOF
}

case $1 in
all)
all
;;
unit)
run_unit_tests
;;
lint)
run_lint
;;

*)
print_usage
;;
esac
