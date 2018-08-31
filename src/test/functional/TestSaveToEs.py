import os
import shutil
import unittest
import logging

from src.main.presentation.preprocess import preprocess
from src.main.presentation.save_to_es import migrate

OUTPUT_PATH = './data'

logging.basicConfig(level=logging.INFO)

class TestPreprocessing(unittest.TestCase):

    def test_preprocessed_questions_are_saved(self):
        migrate('../../../data/raw')