#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: Python is required to run this application.' >&2
  exit 1
 
else
  python3 -m venv .venv
  source .venv/bin/activate 
  pip3 install -r src/requirements.txt
  pip3 install colored
  python3 src/main.py

fi




