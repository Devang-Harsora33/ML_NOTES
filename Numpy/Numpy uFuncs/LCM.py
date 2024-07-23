import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
arr = np.array([3, 6, 9])
arr2 = np.arange(1, 11)
x1 = np.lcm.reduce(arr)
x2 = np.lcm.reduce(arr2)

print(x)
print(x1)#Returns: 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18).
print(x2)