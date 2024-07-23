import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

newarr2 = np.subtract(arr1, arr2)

newarr3 = np.multiply(arr1, arr2)

newarr4 = np.divide(arr1, arr2)

newarr5 = np.power(arr1, arr2)

newarr6 = np.mod(arr1, arr2)

newarr7 = np.divmod(arr1, arr2)

arr3 = np.array([-1, -2, 1, 2, 3, -4])

newarr8 = np.absolute(arr3)

print(newarr)
print(newarr2)
print(newarr3)
print(newarr4)
print(newarr5)
print(newarr6)
print(newarr7)
print(newarr8)