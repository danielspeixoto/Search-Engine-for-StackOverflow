import logging
import unittest

from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.PostIndex import PostIndex
from src.test.examples.questions import question


logging.basicConfig(level=logging.INFO)


class TestConfig(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.index = PostIndex(Config("localhost", "9200")._connection)

    def test_store(self):
        q = question()
        self.index.insert_one(q)

