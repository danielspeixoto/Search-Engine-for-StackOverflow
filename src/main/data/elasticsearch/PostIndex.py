from typing import Iterable

import elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import logging

from src.main.data.elasticsearch.Index import Index
from src.main.domain.model.Question import Question


class PostIndex(Index):

    DOC_TYPE = 'questions'
    INDEX_NAME = 'questions'

    def __init__(self, connection: Elasticsearch):
        super().__init__(connection, PostIndex.INDEX_NAME, PostIndex.DOC_TYPE, self.settings)

    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0,
            "analysis": {
                "analyzer": {
                    "question_analysis": {
                        "tokenizer": "classic",
                        "filter": ["standard", "lowercase", "porter_stem", "stop"],
                        "char_filter": ["html_strip"],
                    }
                }
            }
        },
        "mappings": {
            "questions": {
                "dynamic": "false",
                "properties": {
                    "title": {
                        "type": "text",
                        "analyzer": "question_analysis",
                        "boost": 3
                    },
                    "body": {
                        "type": "text",
                        "analyzer": "question_analysis",
                        "boost": 1
                    },
                    "score": {
                        "type": "float"
                    },
                    "last_activity_date": {
                        "type": "date"
                    },
                    "creation_date": {
                        "type": "date"
                    },
                    "accepted_answer_id": {
                        "type": "keyword"
                    }
                }
            }
        }
    }

    def similar(self, query) -> Iterable[Question]:
        return self.search(PostIndex.DOC_TYPE, {
            "query": {
                "function_score": {
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "multi_match": {
                                        "fields": [
                                            "title^3",
                                            "body"
                                        ],
                                        "type": "most_fields",
                                        "query": query
                                    }
                                }
                            ],
                            "filter": {
                                "exists": {
                                    "field": "accepted_answer_id"
                                }
                            }
                        }
                    },
                    "script_score": {
                        "script": "_score * Math.log(2 + Math.max(0, doc['score'].value))"
                    }
                }
            }
        })

