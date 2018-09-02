import errno
import os
import pickle

from src.main.data.QuestionsReader import QuestionsReader
from src.main.data.WriteRepository import WriteRepository
from src.main.data.dict.BasicQuestionsReader import BasicQuestionsReader
from src.main.domain.model.PreprocessedQuestion import PreprocessedQuestion
from src.main.domain.model.Question import Question
from src.main.domain.vocabulary.CosineSimilarity import CosineSimilarity
import csv
import pandas as pd

from src.main.domain.vocabulary.Similarity import Similarity
from src.main.util.util import to_pandas_df


class PickleRepository(WriteRepository):

    def __init__(self, data_path: str):
        self._data_path = data_path
        self._question_path = self._data_path + "/questions"
        self._preprocessed_question_path = self._data_path + "/preprocessedquestions"
        self._similarity_path = self._data_path + "/similarity"

    def save_questions(self, questions: [Question]):
        PickleRepository.save_obj(self._question_path, questions)

    def save_preprocessed_questions(self, questions: [PreprocessedQuestion]):
        PickleRepository.save_obj(self._preprocessed_question_path, questions)

    def questions_reader(self) -> QuestionsReader:
        questions = PickleRepository.load_obj(self._question_path)
        repo = BasicQuestionsReader(questions)
        return repo

    # TODO: Persist similarity
    def save_similarity(self, similarity: Similarity):
        PickleRepository.save_obj(self._similarity_path, similarity)

    def similarity(self) -> Similarity:
        return PickleRepository.load_obj(self._similarity_path)

    @staticmethod
    def load_obj(path):
        with open(path + '.pkl', 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def save_obj(path, obj_arr: [object]):
        path = path + ".pkl"
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(path, 'wb') as f:
            pickle.dump(obj_arr, f, pickle.HIGHEST_PROTOCOL)
