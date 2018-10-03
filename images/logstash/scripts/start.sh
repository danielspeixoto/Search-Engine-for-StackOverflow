#!/usr/bin/env bash

for i in {60..0}; do
    if curl mysql:3306; then
        echo 'mySQL ready'
        logstash -f /logstash.conf
        break;
    fi
    echo 'MySQL not ready, waiting...'
    sleep 30;
done