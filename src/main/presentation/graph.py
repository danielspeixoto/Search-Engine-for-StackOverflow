import matplotlib.pyplot as plt

from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Analytics import Analytics

recsys_repo = PickleRepository("/home/daniel/ufba/rec/analysis/recsys")
cosine_repo = PickleRepository("/home/daniel/ufba/rec/analysis/cosine")

recsys_analytics = Analytics(recsys_repo)
cosine_analytics = Analytics(cosine_repo)

k_list = range(1, 11)
metrics = {
    "Recall": Analytics.recall,
    "Precision": Analytics.precision,
    "MAP": Analytics.map,
    "F-Measure": Analytics.f_measure
}
for key, value in metrics.items():
    cosine_metrics = cosine_analytics.metrics_at_k(value, k_list)
    recsys_metrics = recsys_analytics.metrics_at_k(value, k_list)
    plt.figure()
    cosine_line, = plt.plot(k_list, cosine_metrics, label='Cosine Similarity')
    recsys_line, = plt.plot(k_list, recsys_metrics, label='RecSys')
    plt.legend(handles=[cosine_line, recsys_line])
    plt.ylabel(key)
    plt.xlabel(key + "@k")
plt.show()
