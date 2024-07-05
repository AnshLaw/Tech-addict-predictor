#!/bin/bash

# Install system-level dependencies
if command -v apt-get >/dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3-tk xvfb xauth
elif command -v dnf >/dev/null; then
    sudo dnf install -y python3-tkinter xorg-x11-server-Xvfb xorg-x11-xauth
fi

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install other dependencies
pip install -r requirements.txt
