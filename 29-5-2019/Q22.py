import numpy as np

np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(precision=5,suppress=True)
print(rand_arr)