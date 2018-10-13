class Model:

    def __init__(self, size, match=["title", "body"], scripted_score=True):
        self.match = match
        self.query = {
            "from": 0,
            "size": size,
            "query": {
                "function_score": {
                    "query": {
                        "bool": {
                            "must": [
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
                    }
                }
            }
        }
        if scripted_score:
            self.query["query"]["function_score"]["script_score"] = {
                "script": "Math.pow(_score, 1) * "
                          "Math.log(2 + Math.max(0, doc['score'].value)) * "
                          "Math.log(1 + doc['answer_count'].value)"
                }

    def get_query(self, question):
        if "title" in self.match:
            self.query["query"]["function_score"]["query"]["bool"]["must"].append(
                {
                    "multi_match": {
                        "fields": [
                            "title",
                        ],
                        "type": "most_fields",
                        "query": question['title']
                    }
                },
            )
        if "body" in self.match:
            self.query["query"]["function_score"]["query"]["bool"]["must"].append(
                {
                    "multi_match": {
                        "fields": [
                            "body",
                        ],
                        "type": "most_fields",
                        "query": question['body']
                    }
                },
            )
        return self.query
