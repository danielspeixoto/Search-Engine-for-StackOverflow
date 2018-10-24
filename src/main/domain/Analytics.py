from src.main.data.interfaces.BulkRepository import BulkRepository


class Analytics:

    def __init__(self, repo: BulkRepository):
        self._data = list(repo.all())

    def metrics_at_k(self, func, k_list: [int]):
        arr = []
        for k in k_list:
            arr.append(
                Analytics.mean(self.metrics_of(func, k))
            )
        return arr

    def metrics_of(self, func, k):
        arr = []
        for analysi in self._data:
            arr.append(func(analysi, k))
        return arr

    @staticmethod
    def mean(arr):
        n = 0
        Sum = 0.0
        for v in arr:
            Sum += v
            n += 1
        return Sum / n

    @staticmethod
    def recall(analysi, k):
        total = 0
        for i in range(k):
            retrieved = analysi['retrieved'][i]
            for expected in analysi['expected']:
                if retrieved == expected:
                    total += 1
        return total/len(analysi['expected'])

    @staticmethod
    def map(analysi, k):
        total = 0
        occurrences = 0
        for i in range(k):
            retrieved = analysi['retrieved'][i]
            for expected in analysi['expected']:
                if retrieved == expected:
                    total += 1/k
                    occurrences += 1
        if occurrences == 0:
            return 0
        return total/occurrences

    @staticmethod
    def precision(analysi, k):
        total = 0
        for i in range(k):
            retrieved = analysi['retrieved'][i]
            for expected in analysi['expected']:
                if retrieved == expected:
                    total += 1
        return total/k

    @staticmethod
    def f_measure(analysi, k) -> float:
        recall = Analytics.recall(analysi, k)
        precision = Analytics.precision(analysi, k)
        if recall + precision == 0:
            return 0
        return 2 * recall * precision / (recall + precision)
