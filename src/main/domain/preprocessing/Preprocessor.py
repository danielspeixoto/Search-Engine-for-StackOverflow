from src.main.data.ReadRepository import ReadRepository
from src.main.data.WriteRepository import WriteRepository
from src.main.domain.preprocessing.QuestionsPreprocessor import QuestionsPreprocessor
from src.main.domain.vocabulary.Similarity import Similarity


class Preprocess:

    def __init__(self,
                 input_data: ReadRepository,
                 output: WriteRepository,
                 similarity: Similarity = Similarity()):
        self.input = input_data
        self.output = output
        self.questions = []
        self.similarity = similarity

    def preprocess(self):
        questions_preprocessor = QuestionsPreprocessor(self.similarity)
        questions = self.input.questions_reader().questions()
        self.questions = questions_preprocessor.preprocess(questions)

    def persist(self):
        self.output.save_questions(self.questions)
        self.output.save_similarity(self.similarity)


