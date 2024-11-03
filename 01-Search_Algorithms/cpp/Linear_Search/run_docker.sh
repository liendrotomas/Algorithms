#!/bin/bash

# Set the image name
IMAGE_NAME="linear_search"

# Build the Docker image
echo "Building Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME .

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Error building Docker image."
    exit 1
fi

# Run the Docker container
echo "Running Docker container from image: $IMAGE_NAME"
docker run -it --rm $IMAGE_NAME

# Check if the container ran successfully
if [ $? -ne 0 ]; then
    echo "Error running Docker container."
    exit 1
fi

echo "Docker container ran successfully."
