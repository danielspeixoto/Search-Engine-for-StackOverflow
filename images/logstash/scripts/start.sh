#!/usr/bin/env bash

while true; do
    if curl mysql:3306 -o output.txt; then
        echo 'mySQL ready'
        logstash -f /logstash.conf
        break;
    fi
    echo 'MySQL not ready, waiting...'
    sleep 30;
done