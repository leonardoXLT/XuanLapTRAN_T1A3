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
pip install colorama
pip install pyfiglet
pip install colored

python main.py