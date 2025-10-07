#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
    brew install python3
    brew install python-tk
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    if [ -f /etc/debian_version ]; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip python3-venv python3-tk
    elif [ -f /etc/redhat-release ]; then
        sudo yum install -y python3 python3-pip tkinter
    elif [ -f /etc/arch-release ]; then
        sudo pacman -Syu --noconfirm python python-pip python-virtualenv tk
    else
        echo "Unsupported Linux distribution. Please install Python 3 and pip manually."
        exit 1
    fi
else
    echo "Unsupported OS."
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
