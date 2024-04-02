#!/bin/bash

xhost +local:root

# Get the absolute path to the directory containing this script
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

# Build the Docker image
docker build -t mechart-dev:latest -f Dockerfile.dev "${SCRIPT_DIR}"

# Start the Docker container
docker run -it \
    --rm \
    -p 5000:5000 \
    --privileged \
    -v "/${SCRIPT_DIR}:/app" \
    -e "OPENAI_API_KEY=$(cat openai-key.txt)" \
    mechart-dev:latest \
    bash
