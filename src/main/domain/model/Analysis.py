class Analysis:

    def __init__(self, question_id: int, retrieved: [int], expected: [int]):
        self.question_id = question_id
        self.retrieved = retrieved
        self.expected = expected

    def map(self):
        i = 0
        map = 0
        amount = 0
        for ret in self.retrieved:
            i += 1
            if ret in self.expected:
               map += 1
               amount += 1

        if amount == 0:
            amount = 1
        return map / amount
