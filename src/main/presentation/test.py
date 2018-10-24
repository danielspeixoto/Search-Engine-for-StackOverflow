from src.main.data.elasticsearch.AnalysisIndex import AnalysisIndex
from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.elasticsearch.model.CosineSearchModel import CosineSearchModel
from src.main.data.elasticsearch.model.RecSysSearchModel import RecSysSearchModel
from src.main.data.elasticsearch.model.SearchModel import SearchModel
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Test import Test


experiments = {
    "recsys": RecSysSearchModel(),
    "cosine": CosineSearchModel()
}

config = Config("localhost", "9200")
for name, model in experiments.items():
    print(name + " analysis running...")
    repo = PickleRepository("/home/daniel/ufba/rec/analysis/" + name)
    index = QuestionIndex(config, model)
    test = Test(index, repo)
    test.test()

