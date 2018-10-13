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

    def query(self, title, body="") -> Iterable[Question]:
        body = title
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
                                            "title",
                                        ],
                                        "type": "most_fields",
                                        "query": title
                                    }
                                },
                                # {
                                #     "multi_match": {
                                #         "fields": [
                                #             "body",
                                #         ],
                                #         "type": "most_fields",
                                #         "query": body
                                #     }
                                # },
                                {
                                    # Questions are only useful when we have a answer to them
                                    "range": {
                                        "answer_count": {
                                            "gte": 0
                                        }
                                    }
                                }
                            ],

                        }
                    },
                    # "script_score": {
                    #     "script": "Math.pow(_score, 1) * "
                    #               "Math.log(2 + Math.max(0, doc['score'].value)) * "
                    #               "Math.log(1 + doc['answer_count'].value)"
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
            "sort": [
                {"id": {"order": "asc"}},
                "_score"
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
