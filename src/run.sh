#!/bin/bash

# check if python is installed

if ! command -v python3 &> /dev/null
then
    echo "Python could not be found. Please install Python 3."
    exit
fi

# check if venv exists

if [ ! -d "mempal-env" ] 
then
    python3 -m venv mempal-env
fi

# Activate the virtual environment and install dependencies and run the application

source mempal-env/bin/activate
pip3 install colorama
pip3 install pyfiglet
pip3 install colored

python3 main.py