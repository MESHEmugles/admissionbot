#!/bin/sh

# Train the model
chmod a+rwx models/
environ/Scripts/activate
rasa train

# Build the rasa and action_server containers
docker compose build [service_name] –-no-cache

# Start the containers
docker compose up -d --force-recreate

# Attach shell to a container
docker exec -it [container_name or ID] bash

# Working with postgres
> psql -U postgres
// List Databases
=# \l