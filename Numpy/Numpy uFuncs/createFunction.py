import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)



x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)


def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.

print(myadd(x, y))
print(type(np.add))
print(type(np.concatenate))
