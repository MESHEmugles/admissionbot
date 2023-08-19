#!/bin/sh

# create the frontend image

sudo docker build . -t frontend -f frontends/Dockerfile

# Create the container and map to port 8000
sudo docker run frontend

# create the rasa image
sudo docker build . -t rasa-backend

# Create the container
sudo docker run rasa-backend
