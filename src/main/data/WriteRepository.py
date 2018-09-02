from src.main.data.ReadRepository import ReadRepository
from src.main.domain.model.PreprocessedQuestion import PreprocessedQuestion
from src.main.domain.model.Question import Question
from src.main.domain.vocabulary.Similarity import Similarity


class WriteRepository(ReadRepository):

    def save_questions(self, questions: [Question]):
        pass

    def save_similarity(self, similarity: Similarity):
        pass

    def save_preprocessed_questions(self, questions: [PreprocessedQuestion]):
        pass