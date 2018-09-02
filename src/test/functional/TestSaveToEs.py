import os
import shutil
import time
import unittest
import logging

from src.main.presentation.preprocess import preprocess
from src.main.presentation.save_to_es import migrate

OUTPUT_PATH = './data'
ubuntu = '/home/daniel/ufba/rec/datasets/stackoverflow/askubuntu.com'
small = '../examples/data/raw'
logging.basicConfig(level=logging.INFO)

class TestPreprocessing(unittest.TestCase):

    def test_preprocessed_questions_are_saved(self):
        init = time.time()
        migrate(small)
        end = time.time()
        duration = end - init
        print(str(duration % (1000 * 60)) + " minutes")