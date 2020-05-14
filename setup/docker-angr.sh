#!/bin/bash

docker run --rm -ti -u angr -v `pwd`/../:/home/angr/symbolic angr/angr bash
