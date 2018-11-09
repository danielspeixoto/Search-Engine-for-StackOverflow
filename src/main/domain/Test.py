from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.interfaces.BulkRepository import BulkRepository
from src.main.domain.model.Analysis import Analysis


class Test:

    def __init__(self, index: QuestionIndex, results: BulkRepository):
        self.index = index
        self.results = results

    def test(self, initial_query_size=10):
        query_size = initial_query_size
        amount_retrieved = 0

        map = 0

        while True:
            questions = self.index.sample_data(amount_retrieved, query_size)
            analysis = []
            for question in questions:
                retrieved = self.index.test(question, 0, 100)
                retrieved = self._questions_id(retrieved)
                expected = question["relations"]
                analysi = Analysis(question['id'], retrieved, expected)
                analysis.append(
                    analysi.__dict__
                )
                map += analysi.map()

            # self.results.save(analysis)
            amount_retrieved = amount_retrieved + len(analysis)
            print("%s done" % amount_retrieved)

            print("Current MAP: " + str(float(map)/amount_retrieved))

            # End of pagination
            if len(analysis) < query_size:
                break

            query_size = len(analysis)

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
