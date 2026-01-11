#!/bin/bash

# Navigate to project directory
cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

echo "Virtual environment activated!"
echo "Python: $(which python)"
echo "Project: DSA (Data Structures & Algorithms)"
echo ""
echo "To deactivate, type: deactivate"

