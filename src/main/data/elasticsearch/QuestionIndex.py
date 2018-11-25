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
        self._query_model = model

    def id(self, id: str):
        return super().search({
            "query": {
                "match": {
                    "id": id
                }
            }
        })

    def query(self, question, start: int, amount: int) -> Iterable[Question]:
        return self.search(self._query_model.query_model()(question, start, amount))

    def query_info(self, question, start: int, amount: int):
        hits = self.search_info(self._query_model.query_model()(question, start, amount))['hits']
        retrieved = hits['total']
        questions = []
        for i in hits['hits']:
            questions.append(i['_source'])
        return retrieved, questions

    def test(self, question, start: int, amount: int) -> Iterable[Question]:
        return self.search(self._query_model.test_model()(question, start, amount))

    def sample_data(self, start: int, amount: int):
        return self.search({
            "from": start, "size": amount,
            "_source": [
                "title",
                "id",
                "body",
                "relations",
                "creation_date"
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
