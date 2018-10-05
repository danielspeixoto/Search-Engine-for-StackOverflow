from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.model.Analysis import Analysis


class Test:

    def __init__(self, index: QuestionIndex, results: PickleRepository):
        self.index = index
        self.results = results

    def test(self):
        amount = 5
        start = 0
        while True:
            questions = self.index.sample_data(start, amount)
            analysis = []
            for question in questions:
                retrieved = self._questions_id(self._query(question))
                expected = question["relations"]
                analysis.append(Analysis(question['id'], retrieved, expected))
            # self.results.save_analysis(analysis

            for analysi in analysis:
                analysi.print()
            # if len(questions) == amount:
            #     break
            start = start + amount
            print(str(start) + " questions analysed")
            break

    def _query(self, question):
        return self.index.query(question['title'])

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
