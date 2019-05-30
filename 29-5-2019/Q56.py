import numpy as np

np.random.seed(100)
a = np.random.randint(1,10, [5,3])
out = [np.max(row) for row in a]
print(out)