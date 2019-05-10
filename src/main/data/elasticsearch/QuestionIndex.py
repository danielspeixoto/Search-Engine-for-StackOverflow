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

    def suggest(self, query):
        sg = self.search_info({
            "suggest": {
                "text": query,
                "suggest": {
                    "term": {
                        # "offset": 5,
                        "suggest_mode": "always",
                        # "lowercase_terms": True,
                        "sort": "frequency",
                        "min_doc_freq": 300,
                        "string_distance": "jaro_winkler",
                        "analyzer": "question_analysis",
                        "field": "title",
                    }
                }
            }
        })["suggest"]["suggest"]

        word_count = len(sg)
        q_word = query.split(" ")
        suggestions = []
        phrase = ""
        phrase2 = ""
        for i in range(word_count):
            last_word = sg[i]["options"]
            suggestion_found = False
            phrase = phrase2
            for options in last_word:
                if len(suggestions) >= 5:
                    break
                if options['score'] < 0.8:
                    continue
                if not suggestion_found:
                    suggestion_found = True
                    phrase2 = phrase + " " + options['text']

                suggest = (phrase + " " + options['text'] + " " + ' '.join(q_word[i + 1:])).strip()
                if suggest not in suggestions:
                    suggestions.append(suggest)
            if not suggestion_found:
                phrase2 += " " + q_word[i]
        return suggestions

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
