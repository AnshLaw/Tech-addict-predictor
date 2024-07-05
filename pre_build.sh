#!/bin/bash

# Install system-level dependencies
if command -v apt-get >/dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3-tk xvfb
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-tkinter xvfb
fi

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install other dependencies
pip install -r requirements.txt
