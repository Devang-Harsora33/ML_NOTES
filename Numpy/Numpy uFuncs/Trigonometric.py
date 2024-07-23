import numpy as np

x = np.sin(np.pi/2)

print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)#degrees to radians

print(x)

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr) #radians to degrees

print(x)

x = np.arcsin(1.0)#NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.

print(x)

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)

base = 3
perp = 4

x = np.hypot(base, perp)#NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.

print(x)