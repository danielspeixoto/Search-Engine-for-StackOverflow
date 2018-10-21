#!/usr/bin/env bash

sudo docker rm --force $(sudo docker container ps -aq)