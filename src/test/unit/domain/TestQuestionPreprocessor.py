import unittest

from src.main.domain.preprocessing.QuestionsPreprocessor import QuestionsPreprocessor
from src.main.domain.vocabulary.CosineSimilarity import CosineSimilarity
from src.main.domain.vocabulary.Similarity import Similarity
from src.main.domain.vocabulary.TextProcessor import TextProcessor
from unittest.mock import MagicMock

from src.test.examples import question, questions


class TestQuestionPreprocessor(unittest.TestCase):

    def test_score(self):
        preprocessor = QuestionsPreprocessor(CosineSimilarity(), TextProcessor())
        q = question()
        score = preprocessor.score(q)

        self.assertEqual(score, 3)

    def test_preprocessing(self):
        sim_mock = Similarity()
        sim_mock.transform = MagicMock(return_value=[1, 2, 3])
        sim_mock.read = MagicMock()

        text_mock = TextProcessor()
        text_mock.preprocess = MagicMock(return_value="abc")

        preprocessor = QuestionsPreprocessor(sim_mock, TextProcessor())

        q = questions()

        result = preprocessor.preprocess(q)
        item1 = preprocessor.preprocess(q)[0]

        self.assertEqual(len(result), len(q))
        self.assertEqual(
            item1.title_doc_term,
            [1, 2, 3]
        )
        self.assertEqual(
            item1.score,
            q[0].score
        )