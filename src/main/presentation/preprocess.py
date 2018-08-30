from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.data.xml.XMLRepository import XMLRepository
from src.main.domain.preprocessing.Preprocessor import Preprocessor
from src.main.domain.vocabulary.CosineSimilarity import CosineSimilarity

def preprocess(input_path: str, output_path: str):
    input = XMLRepository(input_path)
    output = PickleRepository(output_path)
    similarity = CosineSimilarity()
    preprocessor = Preprocessor(input, output, similarity)

    preprocessor.preprocess()
    preprocessor.persist()
