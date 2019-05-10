import logging
from typing import Dict

from elasticsearch import Elasticsearch, helpers
from src.main.data.elasticsearch.Config import Config
from src.main.data.interfaces.BulkRepository import BulkRepository


class Index(BulkRepository):

    def __init__(self, config: Config, index_name: str, doc_type: str):
        self._connection = config.connection
        self._index_name = index_name
        self._doc_type = doc_type

    def typ(self) -> str:
        return self._doc_type

    def create_index(self, settings: Dict):
        try:
            if not self._connection.indices.exists(self._index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
                self._connection.indices.create(index=self._index_name,
                                                ignore=400, body=settings)
                logging.info("Created index: " + self._index_name)
        except Exception as ex:
            logging.error(ex)

    def insert_one(self, record: object) -> Dict:
        outcome = self._connection.index(index=self._index_name, doc_type=self._doc_type, body=record.__dict__)
        return outcome

    def search(self, search):
        res = self._connection.search(index=self._index_name, doc_type=self._doc_type, body=search)["hits"]["hits"]
        for i in res:
            yield i["_source"]

    def search_info(self, search):
        return self._connection.search(index=self._index_name, body=search)

    def save(self, records: [Dict]):
        helpers.bulk(self._connection,
                     records,
                     doc_type=self._doc_type,
                     index=self._index_name)

    def search_by_id(self, id: str):
        # TODO Limit to 1, match exact id
        return self.search({
            "query": {
                "match": {
                    "id": id
                }
            }
        })

    def all(self) -> [object]:
        return self.search({
            "query": {
                "match_all": {}
            }
        })
