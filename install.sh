#!/bin/sh

python3 -m venv virtual_env
source virtual_env/bin/activate
pip install -r requirements.txt
flask db upgrade
export FLASK_APP=main.py
echo "Installation Complete."
