#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 src/main.py

chmod +x src/run.sh

./src/run.sh



