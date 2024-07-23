import numpy as np

arr = np.array([1, 2, 3, 4])
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod(arr)
x1 = np.prod([arr1, arr2])
newarr = np.prod([arr1, arr2], axis=1)
newarr2 = np.cumprod(arr)

print(x)
print(x1)
print(newarr)
print(newarr2)
