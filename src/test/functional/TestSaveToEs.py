import os
import shutil
import time
import unittest
import logging

import nltk
from IPython.display import HTML, display
from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.PostIndex import PostIndex
from src.main.presentation.preprocess import preprocess
from src.main.presentation.save_to_es import migrate

OUTPUT_PATH = './data'
ubuntu = '/home/daniel/ufba/rec/datasets/stackoverflow/askubuntu.com'
small = '../examples/data/raw'
stack = '/home/daniel/ufba/rec/datasets/stackoverflow/stackoverflow/'
logging.basicConfig(level=logging.INFO)


class TestElasticSearch(unittest.TestCase):

    index = None

    def setUp(self):
        super().setUp()
        self.index = PostIndex(Config("localhost", "9200")._connection)

    def test_preprocessed_questions_are_saved(self):
        init = time.time()
        migrate(ubuntu)
        end = time.time()
        duration = end - init
        print(str(duration / 60) + " minutes")

    def test_similar(self):
        index = PostIndex(Config("localhost", "9200")._connection)
        print(index.similar("stack")["hits"]["hits"][0]['_source'])

    def test_search_id(self):
        index = PostIndex(Config("localhost", "9200")._connection)
        print(index.search_by_id(PostIndex.DOC_TYPE, "2")["hits"]["hits"][0]['_source'])

    def test_answers(self):
        index = PostIndex(Config("localhost", "9200")._connection)
        query = "How to delete files recursiverly?"
        results = index.similar(query)["hits"]["hits"]

        view = "<h1>" + query + "</h1>"
        for i in range(min(len(results), 3)):
            question = results[i]['_source']
            title = question['title']
            if title is None or title == '':
                title = question['body']
            view += "\n<br><b>=> Question</b>: " + title + "<br>\n"
            view += "        <b>Answer was:</b>" + "\n"
            answer = index.search_by_id(PostIndex.DOC_TYPE, question['accepted_answer_id'])["hits"]["hits"][0]['_source']
            view += answer['body']
            view += "___________________________________________________________________________________________" + "\n"


        display(view)

    def test_delete(self):
        self.index.delete()