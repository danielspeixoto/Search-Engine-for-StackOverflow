import errno
import os
import pickle

from src.main.domain.model.Analysis import Analysis


class PickleRepository:

    def __init__(self, data_path: str):
        self._data_path = data_path
        self._analysis_path = self._data_path + "/analysis"

    def save_analysis(self, analysis: [Analysis]):
        PickleRepository.save_obj(self._analysis_path, analysis)

    def analysis_reader(self) -> [Analysis]:
        analysis = PickleRepository.load_obj(self._analysis_path)
        return analysis

    @staticmethod
    def load_obj(path):
        with open(path + '.pkl', 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def save_obj(path, obj_arr: [object]):
        path = path + ".pkl"
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(path, 'wb') as f:
            pickle.dump(obj_arr, f, pickle.HIGHEST_PROTOCOL)