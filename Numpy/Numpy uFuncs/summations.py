import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
arr = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)# n outputs as per the array dimensions
newarr1 = np.sum([arr1, arr2])#1 output 
newarr2 = np.sum([arr1, arr2], axis=1)
newarr3 = np.cumsum(arr)#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

print(newarr)
print(newarr1)
print(newarr2)
print(newarr3)