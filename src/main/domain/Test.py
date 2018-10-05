from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.domain.Results import Results


class Test:

    def __init__(self, index: QuestionIndex, results: Results):
        self.index = index
        self.results = results

    def test(self):
        amount = 10
        start = 0
        while True:
            questions = self.index.sample_data(start, amount)
            for question in questions:
                retrieved = self.questions_id(self.query(question))
                expected = question["relations"]
                self.results.save_results(question['id'], retrieved, expected)
            # if len(questions) == amount:
            #     break
            start = start + amount
            break

    def query(self, question):
        return self.index.query(question.title)

    @staticmethod
    def questions_id(questions) -> [int]:
        for question in questions:
            yield question['id']

    @staticmethod
    def precision(related, expected) -> float:
        universe = len(related)
        amount = 0
        for question in related:
            if question in expected:
                amount = amount + 1

        return amount / universe
