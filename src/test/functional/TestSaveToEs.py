import os
import shutil
import time
import unittest
import logging

from IPython.display import HTML, display
from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex

OUTPUT_PATH = './data'
ubuntu = '/home/daniel/ufba/rec/datasets/stackoverflow/askubuntu.com'
small = '../examples/data/raw'
stack = '/home/daniel/ufba/rec/datasets/stackoverflow/stackoverflow/'
logging.basicConfig(level=logging.INFO)


class TestElasticSearch(unittest.TestCase):

    index = None

    def setUp(self):
        super().setUp()
        self.index = QuestionIndex(Config("localhost", "9200")._connection)

    def test_search_id(self):
        # ToDO: Asserts
        index = QuestionIndex(Config("localhost", "9200")._connection)
        print(index.search_by_id(QuestionIndex.DOC_TYPE, "2")["hits"]["hits"][0]['_source'])

    def test_answers(self):
        # ToDO: Asserts
        index = QuestionIndex(Config("localhost", "9200")._connection)
        query = "how to change file permissions?"
        results = index.query(query)

        view = "<h1>" + query + "</h1>"
        for i in results:
            print(i)
            #
            # question = results[i]['_source']
            # title = question['title']
            # if title is None or title == '':
            #     title = question['body']
            # view += "\n<br><b>=> Question</b>: " + title + "<br>\n"
            # view += "        <b>Answer was:</b>" + "\n"
            # # answer = index.search_by_id(QuestionIndex.DOC_TYPE, question['accepted_answer_id'])["hits"]["hits"][0]['_source']
            # # view += answer['body']
            # view += "___________________________________________________________________________________________" + "\n"