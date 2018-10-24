from src.main.data.elasticsearch.AnalysisIndex import AnalysisIndex
from src.main.data.elasticsearch.Config import Config
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Analytics import Analytics

# config = Config("localhost", "9200")
# repo = AnalysisIndex(config, "recsys")
repo = PickleRepository("/home/daniel/ufba/rec/")

analytics = Analytics(repo)

# for i in analytics.recalls(10):
#     print(i)

# print(analytics.mean(analytics.metrics_of(Analytics.recall, 10)))

# print(analytics.metrics_at_k(Analytics.precision, range(1, 11)))

import numpy as np
import matplotlib.pyplot as plt

data = analytics.metrics_of(Analytics.precision, 10)
print(data)

fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(data)

plt.show()