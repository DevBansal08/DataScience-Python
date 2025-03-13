import numpy as np

a = np.array([1,2,3])
print(a.ndim) 

b = np.array([[1,3,5], [23,3,4], [3,4,5]])
print(b.ndim)

c = np.linspace(1,5,10)
print(c)

d = np.array([[6,7,8], [1,2,3], [9,3,2]])
print(d[0:2,2])
