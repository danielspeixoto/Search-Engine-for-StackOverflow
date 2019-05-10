#!/usr/bin/env bash

scripts/lowlevel/config.sh & \
(
docker-compose -f compose/start.yaml up & \
(
    while true; do
        if curl localhost:9200; then
            break;
        fi
        sleep 30;
    done

    rm -rf images/elasticsearch/backups/**
    curl -X PUT "localhost:9200/_snapshot/kibana_backup/first?wait_for_completion=true" \
        -H "Content-Type: application/json" -d @images/elasticsearch/backup.json
    echo 'Backups Kibana'
)
)