#!/usr/bin/env bash

for i in {30..0}; do
    if curl elasticsearch:9200; then
        break;
    fi
    sleep 30;
done

curl -X PUT "elasticsearch:9200/_snapshot/kibana_backup/first?wait_for_completion=true" \
    -H "Content-Type: application/json" -d @/home/backup.json
echo 'Backups Kibana'
