import numpy as np
import pandas as pd
a = np.array([[3,3,3],[4,4,4],[5,5,5]])
b_1d = np.array([1,1,1])
b = (np.r_[np.repeat(b_1d,3)])
b = np.reshape(b,(a.shape[0],a.shape[0]))
print(a-b)