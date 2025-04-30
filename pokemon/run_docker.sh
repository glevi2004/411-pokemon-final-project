#!/bin/bash

# Build the Docker image
docker build -t pokemon-app .

# Run the container
docker run -p 5001:5000 \
  --env-file .env \
  --name pokemon-container \
  pokemon-app
