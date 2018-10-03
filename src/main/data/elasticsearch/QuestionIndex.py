from typing import Iterable

from elasticsearch import Elasticsearch

from src.main.data.elasticsearch.Index import Index
from src.main.domain.model.Question import Question


class QuestionIndex(Index):

    DOC_TYPE = 'questions'
    INDEX_NAME = 'questions'

    def __init__(self, connection: Elasticsearch):
        super().__init__(connection, QuestionIndex.INDEX_NAME, QuestionIndex.DOC_TYPE)

    def id(self, id: str):
        return super().search(QuestionIndex.DOC_TYPE, {
            "query": {
                "match": {
                    "id": id
                }
            }
        })

    def query(self, query) -> Iterable[Question]:
        return self.search(QuestionIndex.DOC_TYPE, {
            "from": 0, "size": 5,
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