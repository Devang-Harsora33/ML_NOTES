import numpy as np

arr = np.trunc([-3.1666, 3.6667])#Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr2 = np.fix([-3.1666, 3.6667])
arr3 = np.around(3.1666, 2)#The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
arr4 = np.floor([-3.1666, 3.6667])#The floor() function rounds off decimal to nearest lower integer.

arr5 = np.ceil([-3.1666, 3.6667])#The ceil() function rounds off decimal to nearest upper integer.
print(arr)
print(arr2)
print(arr3)
print(arr4)
print(arr5)