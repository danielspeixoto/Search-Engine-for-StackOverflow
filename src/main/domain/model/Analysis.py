class Analysis:

    def __init__(self, question_id: int, retrieved: [int], expected: [int]):
        self.question_id = question_id
        self.retrieved = retrieved
        self.expected = expected

    def print(self):
        print("question id: " + str(self.question_id) + " retrieved: " + str(self.retrieved) + " expected: " + str(self.expected))