import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
ages = [np.random.normal(30, 5, 100),
        np.random.normal(40, 5, 100),
        np.random.normal(35, 5, 100)]

plt.boxplot(ages, patch_artist=True, notch=True, vert=True, labels=['Grupo 1', 'Grupo 2', 'Grupo 3']) #patch_artist: caja rellena de color, notch: añadir recorte
plt.title('Distribución de edades por grupo')
plt.xlabel('Grupo')
plt.ylabel('Edad (año)')
plt.show()
