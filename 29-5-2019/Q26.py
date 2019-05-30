import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
#print(iris_1d)
species = np.array([row[4] for row in iris_1d])
print(species[:5])