from copy import copy
from typing import Dict

from src.main.domain.model.Answer import Answer
from src.main.domain.model.Post import Post


class Question(Post):
    ANSWER_COUNT = 'AnswerCount'
    ACCEPTED_ANSWER_ID = 'AcceptedAnswerId'

    def __init__(self, data: Dict[str, str]):
        super().__init__(data)
        self.answer_count: int = self.init_int_var(self.ANSWER_COUNT, data)
        self.accepted_answer_id: str = self.init_var(self.ACCEPTED_ANSWER_ID, data)
        self.answers: [Answer] = []