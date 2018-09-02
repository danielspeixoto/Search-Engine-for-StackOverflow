import unittest

from src.main.data.xml.XMLRepository import XMLRepository


class TestXMLRawRepository(unittest.TestCase):

    def test_init_does_not_breaks(self):
        repo = XMLRepository("../../../examples/data/raw")
        self.assertEqual(len(repo.questions_reader()._questions), 4)
