import numpy as np

#Suma
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

sum = A + B
print(A)
print(B)
print(sum)

#Multiplicación
product = np.dot(A, B)
print(product)

#Determinante
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
print(A)
print(det_A)
print(inv_A)

#Resolver Ax = b
b = np.array([9,11])
x = np.linalg.solve(A,b)
print(x)