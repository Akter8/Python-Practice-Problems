import numpy as np
a = np.repeat(1,10).reshape(2,-1)
b = np.arange(10).reshape(2,-1)
print(a)
print(b)
c = np.hstack((a,b))
print(c)