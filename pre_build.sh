#!/bin/bash

# Install system-level dependencies
if command -v apt-get >/dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3-tk
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-tkinter
elif command -v yum >/dev/null; then
    sudo yum install -y python3-tkinter
fi

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install other dependencies
pip install -r requirements.txt
