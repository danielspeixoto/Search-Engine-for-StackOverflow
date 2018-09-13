#!/usr/bin/env bash

if sudo docker ps -aq; then
    sudo docker rm -f $(sudo docker container ps -aq)
fi
sudo docker-compose build --no-cache
scripts/setup.sh