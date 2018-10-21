#!/usr/bin/env bash

if [ $1 = 'build' ]; then
    sudo docker-compose -f compose/migrate.yaml build
fi
sudo docker-compose -f compose/migrate.yaml  up