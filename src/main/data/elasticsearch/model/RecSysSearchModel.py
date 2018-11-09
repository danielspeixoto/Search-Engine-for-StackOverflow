from src.main.data.elasticsearch.model.SearchModel import SearchModel


class RecSysSearchModel(SearchModel):

    def test_model(self):
        def query(question, start: int=0, size: int=10):
            # print(question)
            return {
                "from": start, "size": size,
                "query": {
                    "function_score": {
                        "query": {
                            "bool": {
                                "must": [
                                    {
                                        "multi_match": {
                                            "fields": [
                                                "title",
                                                "body^3"
                                            ],
                                            "type": "most_fields",
                                            "query": question['body']
                                        }
                                    },
                                    # {
                                    #     "range": {
                                    #         "score": {
                                    #             "gte": 0
                                    #         }
                                    #     },
                                    # },
                                ],
                                "must_not": [
                                    {
                                        "match": {
                                            "id": question['id']
                                        }
                                    }
                                ]
                            }
                        },
                        "functions": [
                            {
                                "script_score": {
                                    "script": "Math.pow(_score, 4) * "
                                              "("
                                              "Math.log(2 + Math.max(0, doc['score'].value)) + "
                                              "Math.log(1 + doc['answer_count'].value)"
                                              ")"
                                }
                            },
                            # {
                            #     "gauss": {
                            #         "creation_date": {
                            #             "origin": question['creation_date'],
                            #             "scale": "300d",
                            #             "offset": "300d",
                            #             "decay": 0.1
                            #         }
                            #     }
                            # }
                        ]
                    }
                }
            }
        return query

    def query_model(self):
        def query(search_query: str, start: int=0, size: int=10):
            return {
                "from": start, "size": size,
                "query": {
                    "function_score": {
                        "query": {
                            "bool": {
                                "must": [
                                    {
                                        "multi_match": {
                                            "fields": [
                                                "title",
                                                "body"
                                            ],
                                            "type": "most_fields",
                                            "query": search_query
                                        }
                                    },
                                    {
                                        "range": {
                                            "score": {
                                                "gte": 0
                                            }
                                        },
                                    },
                                    {
                                        "range": {
                                            "answer_count": {
                                                "gte": 1
                                            }

                                        },
                                    }
                                ]
                            }
                        },
                        "script_score": {
                            "script": "Math.pow(_score, 1) * "
                                      "("
                                      "Math.log(2 + doc['score'].value) + "
                                      "Math.log(1 + doc['answer_count'].value)"
                                      ")"
                        }
                    }
                }
            }
        return query