import numpy as np

np.random.seed(100)
a = np.random.randint(0, 5, 10)
print('Array: ', a)
out = np.zeros(a.shape,dtype=bool)
x, indices = np.unique(a,return_index=True)
out[indices] = True
print(out)