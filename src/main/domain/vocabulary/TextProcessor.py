from nltk.stem.porter import PorterStemmer
import re


class TextProcessor:

    def __init__(self):
        self.stemmer = PorterStemmer()

    def preprocess(self, phrase):
        phrase = phrase.lower()
        # TODO: Allow numbers or not?
        phrase = re.sub('[^a-z]', ' ', phrase)
        phrase = phrase.split()
        # data = [self.stemmer.stem(word) for word in data if word not in self.words_blacklist]
        phrase = [self.stemmer.stem(word) for word in phrase]
        phrase = ' '.join(phrase)
        return phrase

    # Consider n-grams