import numpy as np
a = np.arange(10)
a = np.where(a%2 == 1, -1, a)
print(a)