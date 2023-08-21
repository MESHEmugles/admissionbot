#!/bin/sh

# create the frontend image

sudo docker build ./frontends -t frontend:v1

# Create the container and map to port 8000
sudo docker run -d -t 80:80 frontend

# create the rasa image
sudo docker build . -t rasa-backend:v1

# Create the container
sudo docker run -d -p 5055:5055 rasa-backend:v1
