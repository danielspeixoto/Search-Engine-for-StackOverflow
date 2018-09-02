from src.main.domain.model.Question import Question
from abc import ABCMeta, abstractmethod


class QuestionsReader:

    def max_score(self) -> int:
        pass

    def min_score(self) -> int:
        pass

    def questions(self) -> [Question]:
        pass