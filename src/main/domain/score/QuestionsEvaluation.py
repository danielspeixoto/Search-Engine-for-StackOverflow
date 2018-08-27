from src.main.data.raw.RawRepository import RawRepository
from src.main.domain.model.Question import Question


class QuestionsEvaluation:

    def __init__(self, repository: RawRepository):
        self.repository = repository
        self.questions_repository = repository.questions_repository()
        self.max = self.questions_repository.max_score()
        self.min = self.questions_repository.min_score()
        # TODO Analyze everything so we can evaluate questions on the fly

    def score(self, question) -> Question:
        return 1


