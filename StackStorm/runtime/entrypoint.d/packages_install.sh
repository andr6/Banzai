#!/bin/bash

# install pip - pyton package manager
echo 'Y' | apt-get install python-pip

# install DefectDojo Python module
echo 'Y' | pip install defectdojo_api

# upgrade Python Requests module
pip install -U requests
