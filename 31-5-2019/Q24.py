import numpy as np 
import pandas as pd

def x(l):
    vowels = ['a','e','i','o','u']
    count = 0
    for letter in l:
        if letter.lower() in vowels:
            count += 1
    if count < 2:
        return False
    else:
        return True


ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
y = pd.Series(filter(x,ser))
print(y)