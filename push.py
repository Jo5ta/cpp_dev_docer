#!/usr/bin/env python3
import urllib.request
import json
import subprocess

# Set the URL of the Docker Hub registry API
url = 'https://registry.hub.docker.com/v2/repositories/jo5ta/cpp_dev_docker/tags/?page_size=1'

# Make a request to the API and decode the JSON response
response = urllib.request.urlopen(url).read().decode('utf-8')
data = json.loads(response)

# Extract the version ID of the latest tag and increment the minor version
latest_version = data['results'][0]['name']
major_version, minor_version, *_ = latest_version.split('.')
minor_version = int(minor_version) + 1

# Build and tag the Docker image
image_name = f"jo5ta/cpp_dev_docker:{major_version}.{minor_version:02d}"
command = f"docker build -t {image_name} -f cpp_dev_docker.dockerfile ."
subprocess.run(command, shell=True, check=True)

command = f"docker build -t jo5ta/cpp_dev_docker:latest -f cpp_dev_docker.dockerfile ."
subprocess.run(command, shell=True, check=True)

# Push the Docker image to the registry
command = f"docker push {image_name}"
subprocess.run(command, shell=True, check=True)
command = f"docker push jo5ta/cpp_dev_docker:latest"
subprocess.run(command, shell=True, check=True)
