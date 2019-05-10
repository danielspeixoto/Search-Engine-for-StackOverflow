#!/usr/bin/env bash

sudo docker volume create logstash.
sudo docker volume create es-data
sudo docker volume create mysql