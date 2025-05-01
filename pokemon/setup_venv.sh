#!/bin/bash

# Step 1: Set up the virtual environment
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3: Build and run the Docker container
echo "Building and running Docker container..."
chmod +x run_docker.sh
./run_docker.sh