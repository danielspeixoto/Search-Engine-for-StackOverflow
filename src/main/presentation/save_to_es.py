from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.PostIndex import PostIndex
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.data.xml.XMLRepository import XMLRepository
from src.main.domain.preprocessing.Preprocessor import Preprocessor
from src.main.domain.vocabulary.CosineSimilarity import CosineSimilarity
import logging


def migrate(input_path: str):
    logging.info("getting data")
    input = XMLRepository(input_path)

    index = PostIndex(Config("localhost", "9200")._connection)

    index.bulk_insert(PostIndex.DOC_TYPE, input.questions_reader().questions())
