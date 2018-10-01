#!/usr/bin/env bash

sudo docker-compose -f compose/** down && sudo docker volume rm $(sudo docker volume ls -q)