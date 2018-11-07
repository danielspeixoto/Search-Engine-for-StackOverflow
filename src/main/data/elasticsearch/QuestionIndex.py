from typing import Iterable

from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.Index import Index
from src.main.data.elasticsearch.model.SearchModel import SearchModel
from src.main.domain.model.Question import Question


class QuestionIndex(Index):

    DOC_TYPE = 'questions'
    INDEX_NAME = 'questions'

    def __init__(self, config: Config, model: SearchModel):
        super().__init__(config, QuestionIndex.INDEX_NAME, QuestionIndex.DOC_TYPE)
        self._query_model = model.query_model()

    def id(self, id: str):
        return super().search({
            "query": {
                "match": {
                    "id": id
                }
            }
        })

    def query(self, question, start: int, amount: int) -> Iterable[Question]:
        return self.search(self._query_model(question, start, amount))

    def sample_data(self, start: int, amount: int):
        return self.search({
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
