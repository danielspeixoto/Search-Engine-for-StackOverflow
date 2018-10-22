#!/usr/bin/env bash

scripts/lowlevel/config.sh
if [ $1 = 'build' ]; then
    sudo docker-compose -f compose/populate.yaml build
fi
sudo docker-compose -f compose/populate.yaml up & \
(
    sleep 120;
    while true; do
        if sudo mysql -e "select 1" -h "127.0.0.1" --port 4000 -p --password=admin; then
            echo 'mySQL ready'
            break;
        fi
        echo 'MySQL not ready, waiting...'
        sleep 240;
    done
)
sudo docker-compose -f compose/populate.yaml down && \
scripts/migrate.sh