#!/usr/bin/env bash

sudo docker-compose -f compose/setup.yaml build --no-cache && scripts/setup.sh && scripts/start.sh