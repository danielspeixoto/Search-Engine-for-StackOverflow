from src.main.data.elasticsearch.model.SearchModel import SearchModel


class RecSysSearchModel(SearchModel):

    def query_model(self):
        def query(question, start: int, size: int):
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
                                            "query": question['title']
                                        }
                                    },
                                    {
                                        "range": {
                                            "answer_count": {
                                                "gte": 0
                                            }
                                        }
                                    }
                                ],

                            }
                        },
                        "script_score": {
                            "script": "Math.pow(_score, 1) * "
                                      "Math.log(2 + Math.max(0, doc['score'].value)) * "
                                      "Math.log(1 + doc['answer_count'].value)"
                        }
                    }
                }
            }
        return query