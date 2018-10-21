#!/usr/bin/env bash

scripts/lowlevel/config.sh && \
sudo docker-compose -f compose/populate.yaml up & \
(
#    Time for configuration
    sleep 120
    while true; do
        if mysqladmin --host=127.0.0.1 --port=4000 ping; then
            echo 'mySQL ready'
            break;
        fi
        echo 'MySQL not ready, waiting...'
        sleep 30;
    done
    )
sudo docker-compose -f compose/populate.yaml down && \
sudo docker-compose -f compose/migrate.yaml up