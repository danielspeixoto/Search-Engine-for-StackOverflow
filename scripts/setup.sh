#!/usr/bin/env bash

scripts/lowlevel/config.sh && \
sudo docker-compose -f compose/populate.yaml up && \
sudo docker-compose -f compose/populate.yaml down && \
sudo docker-compose -f compose/migrate.yaml up && \
sudo docker-compose -f compose/migrate.yaml down