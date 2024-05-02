#!/bin/bash

if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: Python is required to run this application.
    Please visit://installpython3.com/ to install.' >&2
  exit 1
fi

if python3 -m venv .venv
then
  source .venv/bin/activate 
  pip3 install -r src/requirements.txt
  pip3 install colored
else
  echo Unable to create virtual environment
fi

python3 src/main.py




