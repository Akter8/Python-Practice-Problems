import numpy as np

np.random.seed(101) 
arr = np.random.randint(1,4, size=6)
print(arr)
uniq = np.unique(arr)
print(uniq)
final = np.zeros((6,3))
#print(final)
for i, j in enumerate(arr):
    final[i,j-1] = 1
print(final)