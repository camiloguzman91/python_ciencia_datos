import numpy as np

array = np.array([[1,2,3],[4,5,6]])
print(array.ndim)
print(array.shape)
print(array.dtype)

z = np.array(3, dtype=np.uint8)
print(z)

double_array = np.array([1,2,3], dtype='d')
print(double_array)

z = z.astype(np.float64)
print(z)

array = np.array([[1,2,3],[4,5,6]])
add = np.sum(array)
print(add)

mean = np.mean(array)
print(mean)

std = np.std(array)
print(std)