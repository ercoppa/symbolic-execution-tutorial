#!/bin/bash

virtualenv -p /usr/bin/python3 ~/.virtualenvs/angr
source ~/.virtualenvs/angr/bin/activate && pip install angr

echo
echo "Angr has been installed."
echo

exit 0
