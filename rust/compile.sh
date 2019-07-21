#!/bin/bash

ROOT=$(dirname ${BASH_SOURCE[0]})

cd ${ROOT}
cargo build --release
cd -