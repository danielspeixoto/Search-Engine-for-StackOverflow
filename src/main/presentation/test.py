from main.data.elasticsearch.model.BM25SearchModel import BM25SearchModel
from src.main.data.elasticsearch.AnalysisIndex import AnalysisIndex
from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.elasticsearch.model.RecSysSearchModel import RecSysSearchModel
from src.main.data.elasticsearch.model.SearchModel import SearchModel
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Test import Test


experiments = {
    "bNoPreprocessing": BM25SearchModel(),
    # "recsysTitle": RecSysSearchModel(1, fields=["title"]),
    # "recsysBody": RecSysSearchModel(1, fields=["body"]),
    # "recsysBoth1": RecSysSearchModel(1),
    # "recsysBoth2": RecSysSearchModel(2),
    # "recsysBoth3": RecSysSearchModel(3),
    # "recsysBoth4": RecSysSearchModel(4),
    # "recsysBoth5NoPreprocessing": RecSysSearchModel(5),
    # "recsysBoth6": RecSysSearchModel(6),
    # "recsysBoth7": RecSysSearchModel(7),
    #BM25 without preprocessing
    #TF/IDF without preprocessing
    #TF/IDF with preprocessing
    #Solution without preprocessing
    #with(out) equation, with(out) preprocessing
}

config = Config("localhost", "9200")
for name, model in experiments.items():
    print(name + " analysis running...")
    repo = PickleRepository("/Users/danielspeixoto/experiments/qa-rec/analysis/" + name)
    index = QuestionIndex(config, model)
    test = Test(index, repo)
    test.test()

