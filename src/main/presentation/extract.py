from src.main.data.elasticsearch.AnalysisIndex import AnalysisIndex
from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.elasticsearch.model.CosineSearchModel import BM25SearchModel
from src.main.data.elasticsearch.model.RecSysSearchModel import RecSysSearchModel
from src.main.data.elasticsearch.model.SearchModel import SearchModel
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Extract import Extract
from src.main.domain.Test import Test


experiments = {
    "recsys": RecSysSearchModel(),
    # "cosine": CosineSearchModel(),
}

config = Config("localhost", "9200")
for name, model in experiments.items():
    print(name + " extraction running...")
    repo = PickleRepository("/Users/danielspeixoto/experiments/qa-rec/" + name)
    index = QuestionIndex(config, model)
    test = Extract(index, repo)
    test.test(max_size=30)

