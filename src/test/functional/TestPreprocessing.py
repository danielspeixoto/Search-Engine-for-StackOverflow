import os
import shutil
import unittest

from src.main.presentation.preprocess import preprocess

OUTPUT_PATH = './data'

class TestPreprocessing(unittest.TestCase):

    def test_preprocessed_questions_are_saved(self):
        preprocess('../examples/data/raw', OUTPUT_PATH)

    def tearDown(self):
        if os.path.exists(os.path.dirname(OUTPUT_PATH)):
            shutil.rmtree(OUTPUT_PATH)