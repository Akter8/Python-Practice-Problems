import numpy as np

np.random.seed(100)
a = np.random.uniform(1,50, 20)

print(a)
print(np.argsort(a)[-5:])