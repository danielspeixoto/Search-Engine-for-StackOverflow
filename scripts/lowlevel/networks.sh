#!/usr/bin/env bash

sudo docker network create elk
sudo docker network create mysql
sudo docker network create data
scripts/setup.sh && scripts/start.sh