#!/usr/bin/env bash

for i in {30..0}; do
    if curl elasticsearch:9200; then
        break;
    fi
    sleep 30;
done
curl -X PUT "elasticsearch:9200/questions" -H 'Content-Type: application/json' -d @/home/questions.json
echo 'Question index config done'
curl -X PUT "elasticsearch:9200/_snapshot/kibana_backup" -H "Content-Type: application/json" -d @/home/kibana_backup.json
echo 'Creates Kibana Backup point'
curl -X POST "elasticsearch:9200/_snapshot/kibana_backup/first/_restore"
echo 'Restores Kibana Backup'

echo 'ElasticSearch config done!'