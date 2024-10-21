import numpy as np

Pepito = np.random.uniform(0,5.1,4)
Josefina = np.random.uniform(0,5.1,4)
Tiburcio = np.random.uniform(0,5.1,4)

P = np.mean(Pepito)
print(Pepito)
print(np.round(P, 2))

J = np.mean(Josefina)
print(Josefina)
print(np.round(J, 2))

T = np.mean(Tiburcio)
print(Tiburcio)
print(np.round(T, 2))

matrix1 = np.array([Pepito, Josefina, Tiburcio])
print(matrix1)


