import numpy as np
import pandas as pd

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

ser = pd.concat((ser1,ser2),axis=1)
ser = pd.Series(np.random.normal(10, 5, 25))
print(ser.quantile)