#!/bin/bash
poetry export > requirements.txt
mkdir -p ./layers/python-dependencies
rm -rf ./layers/python-dependencies
mkdir -p ./layers/python-dependencies/python/lib/python3.7/site-packages
pip install -r requirements.txt -t ./layers/python-dependencies/python/lib/python3.7/site-packages
rm requirements.txt
