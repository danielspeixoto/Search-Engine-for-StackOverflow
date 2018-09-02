import logging

from elasticsearch import Elasticsearch


class Config:

    def __init__(self, host: str, port: str):
        self._connection = self.connect(host, port)

    def connect(self, host: str, port: str) -> Elasticsearch:
        self._connection = Elasticsearch([{'host': host, 'port': port}])
        if self._connection.ping():
            logging.info("Connection to elasticsearch at " + host + ":" + port)
        else:
            logging.error("Could not connect to elasticsearch at " + host + ":" + port)
        return self._connection


