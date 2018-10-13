from src.main.data.pickle.PickleRepository import PickleRepository

repo = PickleRepository("/home/daniel/ufba/rec/")

reader = repo.analysis_reader()

amount_retrieved = 0
map = 0
recall = 0
precision = 0

for analysi in reader:
    map += analysi.map
    recall += analysi.recall
    precision += analysi.precision

    amount_retrieved += 1

    if amount_retrieved % 100 == 0:
        print("Current Results:")
        print("map: " + str(map / amount_retrieved) + " recall: " + str(recall / amount_retrieved) +
              " precision: " + str(precision / amount_retrieved))
        print(str(amount_retrieved) + " questions analysed")