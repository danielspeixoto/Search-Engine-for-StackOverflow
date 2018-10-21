from typing import Iterable, Dict

from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.Index import Index


class AnalysisIndex(Index):

    DOC_TYPE = 'analysis'
    INDEX_NAME = 'analysis'

    def __init__(self, config: Config, model: str):
        super().__init__(config, AnalysisIndex.INDEX_NAME, AnalysisIndex.DOC_TYPE)
        self.model = model
        self.create_index({
          "settings": {
            "index": {
              "number_of_shards": 1,
              "number_of_replicas": 0,
            }
          }
        })

    def save(self, records: [Dict]):
        def put_type():
            for record in records:
                record['model'] = self.model
                yield record
        super().save(put_type())
