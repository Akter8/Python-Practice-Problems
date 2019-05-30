import numpy as np
b = np.arange(10)
a = np.where(b%2 == 1, -1, b)
print(a)
print(b)