#!/bin/bash

# Update pip first
python -m pip install --upgrade pip

# Install required Python packages
pip install python-can pandas streamlit plotly cantools

echo "✅ All prerequisites installed successfully!"