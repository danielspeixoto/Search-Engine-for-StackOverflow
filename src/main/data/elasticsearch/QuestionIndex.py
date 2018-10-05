from typing import Iterable

from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.Index import Index
from src.main.domain.model.Question import Question


class QuestionIndex(Index):

    DOC_TYPE = 'questions'
    INDEX_NAME = 'questions'

    def __init__(self, config: Config):
        super().__init__(config, QuestionIndex.INDEX_NAME, QuestionIndex.DOC_TYPE)

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
            "from": 0, "size": 10,
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
                            # "filter": {
                            #     "exists": {
                            #         "field": "accepted_answer_id"
                            #     }
                            # }
                        }
                    },
                    # "script_score": {
                    #     "script": "_score * Math.log(2 + Math.max(0, doc['score'].value))"
                    # }
                }
            }
        })

    def sample_data(self, start: int, amount: int):
        return self.search(QuestionIndex.DOC_TYPE, {
            "from": start, "size": amount,
            "_source": [
                "title",
                "id",
                "body",
                "relations"
            ],
            "query": {
                "function_score": {
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "match_all": {}
                                }
                            ],
                            "filter": {
                                "script": {
                                    "script": "doc['relations'].values.length > 0"
                                }
                            }
                        }
                    },
                }
            }
        })
