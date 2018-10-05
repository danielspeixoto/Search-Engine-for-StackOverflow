from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Test import Test

repo = PickleRepository("~/ufba/rec/results/")
config = Config("localhost", "9200")
index = QuestionIndex(config)
test = Test(index, repo)

test.test()
