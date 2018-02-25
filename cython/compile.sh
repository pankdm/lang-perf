#!/bin/bash
ROOT=$(dirname ${BASH_SOURCE[0]})
pushd ${ROOT}
python setup.py build_ext --inplace
popd
