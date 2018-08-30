from src.main.data.ReadRepository import ReadRepository
from src.main.data.WriteRepository import WriteRepository
from src.main.domain.model.PreprocessedQuestion import PreprocessedQuestion
from src.main.domain.preprocessing.QuestionsPreprocessor import QuestionsPreprocessor
from src.main.domain.vocabulary.CosineSimilarity import CosineSimilarity
from src.main.domain.vocabulary.Similarity import Similarity
from src.main.domain.vocabulary.TextProcessor import TextProcessor


class Preprocessor:

    def __init__(self,
                 input_data: ReadRepository,
                 output: WriteRepository,
                 similarity: Similarity):
        self._input = input_data
        self._output = output
        self._questions = self._input.questions_reader().questions()
        self._preprocessed_questions = [PreprocessedQuestion]
        self._similarity = similarity

    def preprocess(self):
        questions_preprocessor = QuestionsPreprocessor(
            self._similarity, TextProcessor())
        self._preprocessed_questions = \
            questions_preprocessor.preprocess(self._questions)

    def persist(self):
        self._output.save_questions(self._questions)
        self._output.save_preprocessed_questions(
            self._preprocessed_questions)
        self._output.save_similarity(self._similarity)