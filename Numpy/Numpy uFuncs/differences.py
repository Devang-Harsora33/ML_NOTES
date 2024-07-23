import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)
newarr2 = np.diff(arr, n=2)

print(newarr)
print(newarr2)