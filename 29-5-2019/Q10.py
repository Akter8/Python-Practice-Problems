import numpy as np
a = np.array([1,2,3])
b = np.hstack((a,a))
c = np.hstack((b,a))
c = np.sort(c)
c = np.hstack((c,a))
c = np.hstack((c,a))
c = np.hstack((c,a))
print(c)
d = np.r_[np.repeat(a,3)]
print(d)