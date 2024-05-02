#!/bin/bash

if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: Python is required to run this wpplication.
    Please visit://installpython3.com/ to install.' >&2
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate

pip3 install colored

python3 src/main.py




