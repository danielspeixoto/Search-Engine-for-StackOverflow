from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.model.Analysis import Analysis


class Test:

    def __init__(self, index: QuestionIndex, results: PickleRepository):
        self.index = index
        self.results = results

    def test(self, initial_query_size=100):
        query_size = initial_query_size
        amount_retrieved = 0

        map = 0
        recall = 0
        while True:
            questions = self.index.sample_data(amount_retrieved, query_size)
            analysis = []
            for question in questions:
                retrieved = self._questions_id(self._query(question))
                expected = question["relations"]
                analysis.append(Analysis(question['id'], retrieved, expected))

            query_size = len(analysis)
            amount_retrieved = amount_retrieved + query_size

            for analysi in analysis:
                analysi.print()
                map += analysi.map
                recall += analysi.recall

            print("Current Results:")
            print("map: " + str(map/amount_retrieved) + " recall: " + str(recall/amount_retrieved))
            print(str(amount_retrieved) + " questions analysed")
            # End of pagination
            if len(analysis) < query_size:
                break

    def _query(self, question):
        return self.index.query(question['title'], question['body'])

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
