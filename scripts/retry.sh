#!/usr/bin/env bash

sudo docker-compose -f compose/setup.yaml build && scripts/setup.sh && scripts/start.sh