import datetime
import errno
import os
import pickle
from typing import Dict

from src.main.data.interfaces.BulkRepository import BulkRepository
from src.main.domain.model.Analysis import Analysis


class PickleRepository(BulkRepository):

    def __init__(self, data_path: str):
        self._data_path = data_path
        self._analysis_path = self._data_path + "/analysis"
        self._is_open = False
        self.file = None

    def save(self, analysis: [Analysis]):
        if self.file is None:
            print("Creating file")
            self.file = PickleRepository.create(self._analysis_path)
        self.write(self.file, analysis)

    def close(self):
        self.file.close()

    def write(self, file,  analysis: [Analysis]):
        pickle.dump(analysis, file, protocol=2)

    def all(self) -> [Analysis]:
        analysis = PickleRepository.load_obj(self._analysis_path)
        return analysis

    @staticmethod
    def load_obj(path):
        with open(path + '.pkl', 'rb') as f:
            while True:
                try:
                    for obj in pickle.load(f):
                       yield obj
                except EOFError:
                    break

    @staticmethod
    def create(path):
        path = path + ".pkl"
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        return open(path, "wb")
