import pandas as pd
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
x = pd.Series(mylist)
y = pd.Series(myarr)
z = pd.Series(mydict)