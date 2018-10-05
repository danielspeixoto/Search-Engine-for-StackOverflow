#!/usr/bin/env bash

scripts/lowlevel/config.sh && \
sudo docker-compose -f compose/setup.yaml up  --force-recreate --build