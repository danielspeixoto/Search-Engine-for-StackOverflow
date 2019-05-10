import matplotlib.pyplot as plt

from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Analytics import Analytics

comparisons = [
    {
        "doc": "booleanNoPreprocessing",
        "name": "Booleano sem Pré-Processamento"
    },
    {
        "doc": "bm25NoPreprocessing",
        "name": "BM25 sem Pré-Processamento"
    },
    # {
    #     "doc": "tfidfNoPreprocessing",
    #     "name": "TF/IDF sem Pré-Processamento"
    # },
    # {
    #     "doc": "bNoPreprocessing",
    #     "name": "Booleano com Pré-Processamento"
    # },
    # {
    #     "doc": "bm25Preprocessing",
    #     "name": "BM25 com Pré-Processamento"
    # },
    # {
    #     "doc": "tfidfPreprocessing",
    #     "name": "TF/IDF com Pré-Processamento"
    # },
    # {
    #     "doc": "recsysBoth1",
    #     "name": "Proposta com i=1"
    # },
    # {
    #     "doc": "recsysBoth5",
    #     "name": "Proposta com i=5"
    # },
    # {
    #     "doc": "recsysBoth5NoPreprocessing",
    #     "name": "Proposta com i=5 sem Pré-Processamento"
    # },
]

# comparisons = [
#     {
#         "doc": "recsysTitle",
#         "name": "Título"
#     },
#     {
#         "doc": "recsysBody",
#         "name": "Corpo"
#     },
#     {
#         "doc": "recsysBoth1",
#         "name": "Título + Corpo"
#     }
# ]

# comparisons = [
#     {
#         "doc": "recsysBoth1",
#         "name": "i=1"
#     },
#     {
#         "doc": "recsysBoth2",
#         "name": "i=2"
#     },
#     {
#         "doc": "recsysBoth3",
#         "name": "i=3"
#     },
#     {
#         "doc": "recsysBoth4",
#         "name": "i=4"
#     },
#     {
#         "doc": "recsysBoth5",
#         "name": "i=5"
#     },
#     {
#         "doc": "recsysBoth6",
#         "name": "i=6"
#     },
#     {
#         "doc": "recsysBoth7",
#         "name": "i=7"
#     },
# ]

# comparisons.reverse()
print("dvvsd dsf ")

k_list = range(1, 11)
metrics = {
    "Recall": Analytics.recall,
    "Precision": Analytics.precision,
    # "MRR": Analytics.map,
    "F-Measure": Analytics.f_measure
}
line = []

plt.subplots(3, 1, sharex=True)
for key, value in metrics.items():
    lines = []
    # plt.figure()
    for comp in comparisons:
        repo = PickleRepository(
            "/Users/danielspeixoto/experiments/qa-rec/analysis/" +
            comp["doc"])

        # all = repo.all()
        # # print(len(all))
        # count = 0
        # i = 0
        # for a in repo.all():
        #     i += 1
        #     # if len(a['expected']) == 1:
        #     #     count += 1
        #     count += len(a['retrieved'])
        # print(count / i)
        # exit(1)

        analytics = Analytics(repo)
        metrics = analytics.metrics_at_k(value, k_list)
        line, = plt.plot(k_list, metrics, label=comp["name"], linewidth=1.0)
        lines.append(line)
    plt.legend(handles=lines, bbox_to_anchor=(0, 1.02, 1, 0.2), mode='expand', loc="lower left")
    plt.ylabel(key)
    plt.xlabel(key + "@K")
    # plt.savefig(key + ".png", bbox_inches = 'tight')
plt.show()
#
# recsys_repo = PickleRepository("/Users/danielspeixoto/experiments/qa-rec/analysis/recsys")
# cosine_repo = PickleRepository("/Users/danielspeixoto/experiments/qa-rec/analysis/cosine")
#
# recsys_analytics = Analytics(recsys_repo)
# cosine_analytics = Analytics(cosine_repo)
#
# for key, value in metrics.items():
#     cosine_metrics = cosine_analytics.metrics_at_k(value, k_list)
#     recsys_metrics = recsys_analytics.metrics_at_k(value, k_list)
#     plt.figure()
#     cosine_line, = plt.plot(k_list, cosine_metrics, label='BM25 + Pré-processamento')
#     recsys_line, = plt.plot(k_list, recsys_metrics, label='RecSys')
#     plt.legend(handles=[cosine_line, recsys_line])
#     plt.ylabel(key)
#     plt.xlabel(key + "@k")
# plt.show()
