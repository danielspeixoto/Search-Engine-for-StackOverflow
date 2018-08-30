from copy import deepcopy

from src.main.domain.model.PreprocessedQuestion import PreprocessedQuestion
from src.main.domain.model.Question import Question
from src.main.domain.vocabulary.CosineSimilarity import CosineSimilarity
from src.main.domain.vocabulary.Similarity import Similarity
from src.main.domain.vocabulary.TextProcessor import TextProcessor


class QuestionsPreprocessor:

    def __init__(self, similarity: Similarity,
                 text_processor: TextProcessor):
        self._similarity = similarity
        self._text_processor = text_processor

    def preprocess(self, questions: [Question]) -> [PreprocessedQuestion]:
        corpus: [str] = []
        copied_questions: [Question] = []
        # TODO: Parallelize get_question preprocessing
        for question in questions:
            c_question = deepcopy(question)
            c_question.body = self._text_processor.preprocess(question.body)
            c_question.title = self._text_processor.preprocess(question.title)
            copied_questions.append(c_question)
            corpus.append(c_question.body)
            corpus.append(c_question.title)
        self._similarity.read(corpus)
        preprocessed = self.transform(copied_questions)
        return preprocessed

    def transform(self, questions: [Question]) -> [PreprocessedQuestion]:
        preprocessed: [PreprocessedQuestion] = []
        for question in questions:
            score = self.score(question)
            p_question = PreprocessedQuestion(
                question.id, score, question.title, question.body)
            preprocessed.append(p_question)
        return preprocessed

    def score(self, question: Question) -> float:
        # TODO: Implement scoring
        return question.score

