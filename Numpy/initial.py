import numpy as np

arr = np.array([1, 2, 3, 4, 5, 0])
arr2 = np.array(45) #0D
arr3 = np.array((1, 2, 3, 4,5)) #1D
arr4 = np.array([[1, 2, 3], [4, 5, 6]]) #2D
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])#3D
arr6 = np.array([1, 2, 3, 4], ndmin=5) # custom dimensionality
arr7 = np.array(['apple', 'banana', 'cherry'])
arr8 = np.array([1, 2, 3, 4], dtype='S') #data type string
arr9 = np.array([1, 2, 3, 4], dtype='i4') #data type 4 bytes integer
arr10 = arr.copy()
arr10[0] = 100
arr11 = arr.view()
arr[0] = 100
arr12 = np.concatenate((arr, arr3))
arr13 = np.array([[1, 2, 3], [4, 5, 6]]) #2D
arr14 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr15 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

x = arr[[True, False, False, False, False, True]]
print(x)
filter_arr = []
filter_arr2 = arr % 2 == 0
print(arr)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(type(arr))
print(type(arr3))
print(np.__version__)
newarr = arr.astype("i")
newarr2 = arr.astype(int)
newarr3 = arr.astype(bool)

print(arr.ndim) #number of dimensions
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)
print(arr6.ndim)

print('2nd element on 1st row: ', arr4[0, 1])#2D INDEXING
print('3rd element on 1st arrays 2nd row: ', arr5[0, 1, 2])#3D INDEXING
print('Last element from 2nd dim: ', arr4[1, -1])
print(arr[0:5:2])
print(arr4[1, 1:])
print(arr4[0:2, 2])
print(arr4[0:2, 1:4])
print(arr.dtype)
print(arr7.dtype)
print(arr8.dtype)
print(arr9.dtype)
print(newarr)
print(newarr.dtype)
print(newarr2.dtype)
print(newarr3)
print(newarr3.dtype)
print(arr)
print(arr10)
print(arr11)
print(arr5.shape)
print(arr.reshape(2, 3))
print(arr.reshape(2, 3).base)
print(arr.reshape(2, 3, -1))
print(arr4.reshape(-1))


for x in arr:
    print(x)

for x in arr4:
  for y in x:
    print(y)

for x in arr5:
  print(x)

for x in arr5:
  for y in x:
    for z in y:
      print(z)

for x in np.nditer(arr5):
  print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

for x in np.nditer(arr4[:, ::2]):
  print(x)

for idx, x in np.ndenumerate(arr):
  print(idx , x)


for idx, x in np.ndenumerate(arr4):
  print(idx, x)

for x in arr:
  if x > 3:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr4 = arr[filter_arr]
newarr5 = arr[filter_arr2]

print(arr12)
print(np.concatenate((arr4, arr13), axis=1))
print(np.stack((arr8, arr9), axis=1))
print(np.hstack((arr8, arr9))) #rows
print(np.vstack((arr8, arr9))) #columns
print(np.dstack((arr8, arr9))) #height
print(np.array_split(arr, 3)) #split
print(np.array_split(arr14, 3))
print(np.hsplit(arr15, 3))
print(np.where(arr == 4))
print(np.where(arr%2 == 0))
print(np.where(arr%2 == 1))
print(np.searchsorted(arr, 4))
print(np.searchsorted(arr, 4,side="right"))
print(np.searchsorted(arr, [3,8, 6]))
print(np.sort(arr7))
print(np.sort(arr4))
print(x)
print(filter_arr)
print(newarr4)
print(newarr5)

