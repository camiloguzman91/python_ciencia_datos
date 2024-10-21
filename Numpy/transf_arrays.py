import numpy as np

#Matriz transpuesta
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
transposed_matrix = matrix.T
print(matrix)
print(transposed_matrix)

#Cambio de forma (reshape)
array_s = np.arange(1, 13)
reshaped_array = array_s.reshape(3,4)
print(array_s)
print(reshaped_array)

#Invertir array
reversed_array = array_s[::-1]
print(array_s)
print(reversed_array)

#Aplanamiento de arrays (flattening)
matrix_f = np.array([[1,2,3],[4,5,6],[7,8,9]])
flattened_array = matrix_f.flatten()
print(matrix_f)
print(flattened_array)