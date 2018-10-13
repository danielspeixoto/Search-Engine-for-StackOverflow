from math import nan


class Analysis:

    def __init__(self, question_id: int, retrieved: [int], expected: [int]):
        self.question_id = question_id
        self.retrieved = retrieved
        self.expected = expected
        self.map = 0
        self.recall = 0
        self.precision = 0
        self._calculate()

    def print(self):
        print("question id: " + str(self.question_id) + " retrieved: " + str(self.retrieved) + " expected: " + str(self.expected))
        print("map: " + str(self.map) + " recall: " + str(self.recall))

    def _calculate(self):
        i = 0
        found = 0
        for x in self.retrieved:
            i = i + 1
            for y in self.expected:
                if x == y:
                    found = found + 1
                    self.map = self.map + found / i
        if found != 0:
            self.map /= found
        self.precision = found / len(self.retrieved)
        self.recall = found / len(self.expected)
