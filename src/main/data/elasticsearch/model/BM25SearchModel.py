from src.main.data.elasticsearch.model.SearchModel import SearchModel


class BM25SearchModel(SearchModel):

    def test_model(self):
        def query(question, start: int = 0, size: int = 10):
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
                                            "query": question["title"]
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
                                "must_not": [
                                    {
                                        "match": {
                                            "id": question['id']
                                        }
                                    }
                                ]

                            }
                        }
                    }
                }
            }

        return query