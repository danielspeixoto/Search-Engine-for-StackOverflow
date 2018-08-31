from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.data.xml.XMLRepository import XMLRepository
from src.main.domain.preprocessing.Preprocessor import Preprocessor
from src.main.domain.vocabulary.CosineSimilarity import CosineSimilarity
import logging


def migrate(input_path: str):
    logging.info("getting data")
    input = XMLRepository(input_path)

    index = QuestionIndex(Config("localhost", "9200")._connection)

    for q in input.questions_reader().questions():
        index.store(q)