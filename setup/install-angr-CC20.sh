#!/bin/bash

virtualenv -p /usr/bin/python2.7 ~/.virtualenv/angr2
source ~/.virtualenv/angr2/bin/activate && pip install gitdb2==2.0.6 GitPython==2.1.14 angr

echo
echo "Angr has been installed."
echo

exit 0
