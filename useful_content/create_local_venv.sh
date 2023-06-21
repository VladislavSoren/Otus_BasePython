#!/bin/bash

# set name of venv
export VENV_NAME="venv"

#Create venv without pip
python3 -m venv --without-pip $VENV_NAME

# Get pip in your env
source $VENV_NAME/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
source $VENV_NAME/bin/activate
