from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from src.main.domain.vocabulary.Similarity import Similarity


class CosineSimilarity(Similarity):

    def __init__(self):
        self._vectorizer = TfidfVectorizer()

    def read(self, docs: [str]):
        self._vectorizer.fit(docs)

    def transform(self, word: str):
        result = self._vectorizer.transform([word])[0]
        return result

    def compare(self, str1: str, str2: str) -> float:
        similarity = cosine_similarity(str1, str2)[0][0]
        return similarity
