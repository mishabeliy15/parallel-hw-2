#!/bin/bash

seq 1 "$1" | xargs -n1 -P8 bash -c "curl -O -s $2"

