#!/bin/sh

# Install publishing dependecies
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine

# Build & upload
python3 -m build
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
