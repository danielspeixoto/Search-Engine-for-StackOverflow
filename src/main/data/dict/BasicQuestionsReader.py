from src.main.data.QuestionsReader import QuestionsReader
from src.main.domain.model.Question import Question
from typing import Dict, Iterable, Callable


class BasicQuestionsReader(QuestionsReader):

    def __init__(self, questions: Callable[[], Iterable[Question]]):
        self._questions = questions

    def questions(self) -> Iterable[Question]:
        return self._questions()
