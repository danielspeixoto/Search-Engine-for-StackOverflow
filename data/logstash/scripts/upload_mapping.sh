#!/usr/bin/env bash
curl -XPUT http://elasticsearch:9200/_template/questions_template?pretty -d @mapping.json
