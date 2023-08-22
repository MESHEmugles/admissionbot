#!/bin/sh

# Train the model
chmod a+rwx models/
environ/Scripts/activate
rasa train

# Build the rasa and action_server containers
docker compose build rasa –-no-cache

# Start the containers
docker compose up -d --force-recreate