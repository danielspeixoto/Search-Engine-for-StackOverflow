#!/usr/bin/env bash

sudo docker rm --force $(sudo docker container ps -aq) && sudo docker volume rm $(sudo docker volume ls -q)