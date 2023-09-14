#!/usr/bin/env bash

# Volumes
echo "Creating dedicated volumes"
docker volume create --driver=local jam_sqldb


# Networks
echo "Creating dedicated networks"
docker network create --attachable jam_network

