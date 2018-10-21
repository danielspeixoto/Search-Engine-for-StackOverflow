#!/usr/bin/env bash

while true; do
    if nc -z mysql 3306; then
        echo 'mySQL ready'
        logstash -f /logstash.conf
        break;
    fi
    echo 'MySQL not ready, waiting...'
    sleep 30;
done