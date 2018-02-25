#!/bin/bash
ROOT=$(dirname ${BASH_SOURCE[0]})

mkdir -p ${ROOT}/../build
g++ -std=c++14 -O3 ${ROOT}/solver.cpp -o ${ROOT}/../build/cpp_solver.out
