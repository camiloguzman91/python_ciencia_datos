import numpy as np
import pandas as pd
import matplotlib.pyplot

escalar = np.array(42)
print(type(escalar))
print(escalar)

vector = np.array([30 , 85, 15, 55, 36, 22, 42])
print(vector)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

tensor = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)

array_arange = np.arange(10)
print(array_arange)

eye_matrix = np.eye(7) #Matriz identidad del número
print(eye_matrix)

diag = np.diag([1,2,3,4])
print(diag)

random = np.random.random((2,3))
print(random)