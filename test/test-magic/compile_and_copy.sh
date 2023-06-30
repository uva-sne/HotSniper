#!/bin/bash

# run from docker
make && cp ./fft $GRAPHITE_ROOT/benchmarks/parsec/parsec-2.1/pkgs/apps/blackscholes/inst/amd64-linux.gcc-sniper/bin/blackscholes
