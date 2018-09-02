from abc import abstractmethod

from src.main.data.QuestionsReader import QuestionsReader


class ReadRepository:

    def questions_reader(self) -> QuestionsReader:
        pass

