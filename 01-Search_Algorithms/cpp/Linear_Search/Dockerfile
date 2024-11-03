# Use an official GCC image as a parent image
FROM gcc:latest

# Install necessary packages
RUN apt-get update && apt-get install -y cmake git


# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Run CMake to configure and build the project
RUN cd /app
RUN cmake -S . -B build
RUN cmake --build build

# Run the main program by default
CMD ["./build/main_program"]
