#!/usr/bin/env bash

scripts/lowlevel/config.sh && \
sudo docker-compose -f compose/start.yaml up