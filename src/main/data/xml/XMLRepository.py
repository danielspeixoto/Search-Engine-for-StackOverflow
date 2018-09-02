import logging
from typing import Dict, Iterable, Iterator
import xml.etree.ElementTree as ETree
from xml.etree.ElementTree import ElementTree

from src.main.data.ReadRepository import ReadRepository
from src.main.data.dict.BasicQuestionsReader import BasicQuestionsReader
from src.main.domain.model.Question import Question


class XMLRepository(ReadRepository):
    POSTS = "Posts"

    def __init__(self, data_path: str):
        self.data_path = data_path
        self.paths = [self.POSTS]
        # Type -> List of Dicts
        self.dict: Dict[str,
                        list[
                            Dict[str,
                                 str]
                        ]] = {}
        questions: () = None
        for path in self.paths:
            logging.info("Retrieving xml objects at " + path)
            content = self.retrieve(path)
            logging.info("Parsing xml")
            questions = self.question_xml_to_df(content)
            logging.info("")
        self.questions_repo = BasicQuestionsReader(questions)

    def question_xml_to_df(self, xml: Iterator) -> ():
        # noinspection PyTypeChecker
        def question():
            for event, row in xml:
                # row = xml[i]
                post = row.attrib
                # TODO: Change Retrieving answers as questions
                # if self.is_question(post):
                yield Question(post)
        return question

    def retrieve(self, path: str) -> Iterator:
        return ETree.iterparse(self.data_path + "/" + path + ".xml")

    @staticmethod
    def is_question(question: Dict[str, str]) -> bool:
        return "ParentId" not in question

    def questions_reader(self) -> BasicQuestionsReader:
        return self.questions_repo
