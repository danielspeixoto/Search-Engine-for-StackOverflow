from src.main.data.ReadRepository import ReadRepository
from src.main.domain.model.Question import Question
from src.main.domain.vocabulary.Similarity import Similarity


class QuestionsPreprocessor:

    def __init__(self, similarity: Similarity):
        self.similarity = similarity

    def score(self, question: Question) -> Question:
        # TODO: Implement scoring
        return question

    def preprocess(self, questions: [Question]) -> [Question]:
        preprocessed = []
        # TODO: Parallelize question preprocessing
        for question in questions:
            preprocessed.append(self.preprocess_one(question))
        return preprocessed

    def preprocess_one(self, question: Question) -> Question:
        question = self.score(question)
        self.similarity.read(question.body)
        self.similarity.read(question.title)
        return question


