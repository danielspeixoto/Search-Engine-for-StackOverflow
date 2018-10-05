class Results:

    def save_results(self, question_id: int, retrieved: [int], expected: [int]):
        print("question id: " + str(question_id) + " retrieved: " + str(retrieved) + " expected: " + str(expected))