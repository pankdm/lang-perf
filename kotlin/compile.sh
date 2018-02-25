#!/bin/bash
ROOT=$(dirname ${BASH_SOURCE[0]})

kotlinc ${ROOT}/solver.kt -include-runtime -d build/solver.jar
