import unittest

from src.main.data.elasticsearch.Config import Config


class TestConfig(unittest.TestCase):

    config = None

    def setUp(self):
        super().setUp()
        self.config = Config("localhost", "9200")

    def test_index_creation(self):
        self.config.create_index()

    def test_store(self):
        self.config.store({"title": "test"})