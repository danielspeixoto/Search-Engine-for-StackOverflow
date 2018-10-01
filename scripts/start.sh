#!/usr/bin/env bash

sudo sysctl -w vm.max_map_count=262144 && sudo docker-compose -f compose/setup.yaml up