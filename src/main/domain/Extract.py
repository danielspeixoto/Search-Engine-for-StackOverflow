from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.interfaces.BulkRepository import BulkRepository
import re

class Extract:

    def __init__(self, index: QuestionIndex, results: BulkRepository):
        self.index = index
        self.results = results

    def test(self, initial_query_size=100, max_size=-1):
        query_size = initial_query_size
        amount_retrieved = 0

        while True:
            questions = self.index.sample_data(amount_retrieved, query_size)
            searches = []
            for question in questions:
                retrieved = self._query(question['title'])
                expected = self.index.id(question["relations"][0])

                retrieved = [self._simplify(r) for r in retrieved]
                expected = [self._simplify(r) for r in expected]
                if question["relations"][0] in Extract._questions_id(retrieved):
                    searches.append(
                        {
                            "query": question['title'],
                            "retrieved": retrieved,
                            "expected": expected
                        }
                    )
            self.results.save(searches)

            amount_retrieved = amount_retrieved + len(searches)

            print("%s done" % amount_retrieved)

            # End of pagination
            if max_size != -1 and len(searches) >= max_size:
                break
            if len(searches) < query_size:
                break

            query_size = len(searches)


    def _simplify(self, question):
        return {
            "id": question['id'],
            "title": question['title'],
            # "body": question['body'],
            "tags": re.sub('<', '', question['tags'][0]).split('>')[:-1]
        }

    def _query(self, question):
        return self.index.query(question, 0, 10)

    @staticmethod
    def _questions_id(questions) -> [int]:
        ids = []
        for question in questions:
            ids.append(question['id'])
        return ids

    @staticmethod
    def _precision(related, expected) -> float:
        universe = len(related)
        amount = 0
        for question in related:
            if question in expected:
                amount = amount + 1

        return amount / universe
