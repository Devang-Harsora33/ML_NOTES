import numpy as np
from math import log

arr = np.arange(1, 10)#Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
print(arr)
print(np.log2(arr))#Use the log2() function to perform log at the base 2.
print(np.log10(arr))#Use the log10() function to perform log at the base 10.
print(np.log(arr))#Use the log() function to perform log at the base e.


nplog = np.frompyfunc(log, 2, 1)#NumPy does not provide any function to take log at any base, 
#so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:

print(nplog(2, 10))

