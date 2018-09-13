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
        super().__init__(connection, PostIndex.INDEX_NAME, PostIndex.DOC_TYPE)

    def query(self, query) -> Iterable[Question]:
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