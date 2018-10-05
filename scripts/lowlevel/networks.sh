#!/usr/bin/env bash

sudo docker network create elk
sudo docker network create mysql
scripts/setup.sh && scripts/start.sh