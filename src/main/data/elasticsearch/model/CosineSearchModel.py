from src.main.data.elasticsearch.model.SearchModel import SearchModel


class CosineSearchModel(SearchModel):

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
                                            "query": question
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
                        }
                    }
                }
            }

        return query