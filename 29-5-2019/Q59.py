import numpy as np

def x(a):
    if np.isnan(a):
        print(a)
        return True
    else:
        return False    

    

a = np.array([1,2,3,4,5,6,7,np.nan])
y = np.vectorize(x)
a = a[~y(a)]
print(a)