import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6,7,7,8])
b = np.where((a>5) & (a<10))
print(a[b])