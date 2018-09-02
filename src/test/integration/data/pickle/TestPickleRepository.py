import os
import unittest

from src.main.data.pickle.PickleRepository import PickleRepository
from src.test.examples import questions

repo = PickleRepository('./data')

PATH = './data/loadobjs'


class TestPickleRepository(unittest.TestCase):

    def test_saved_data_can_be_retrieved(self):
        q = questions()

        repo.save_obj(PATH, q)
        result = repo.load_obj(PATH)

        self.assertEqual(q, result)

    def tearDown(self):
        if os.path.exists(os.path.dirname(PATH + '.pkl  ')):
            os.remove(PATH + '.pkl')

