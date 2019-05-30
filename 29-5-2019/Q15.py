import numpy as np
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

xy = np.vectorize(maxx)

a = np.arange(10)
b = a[::-1]
c = xy(a,b)
print(a,b,c)