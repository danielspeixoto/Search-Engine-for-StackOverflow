#!/usr/bin/env bash

for i in {30..0}; do
    if nc -z  elasticsearch:9200; then
        curl -X PUT "elasticsearch:9200/questions" -H 'Content-Type: application/json' -d @questions.json
        break;
    fi
    sleep 30;
done
echo 'Index config done!'