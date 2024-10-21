import numpy as np
import matplotlib.pyplot as plt

data =np.random.normal(170, 10, 200)
print(data)

plt.hist(data, color='salmon', bins= 5, edgecolor='black', alpha=0.6) #alpha: transparencia de datos
plt.title('Distribución de alturas')
plt.xlabel('Atura (cm)')
plt.ylabel('Densidad')
plt.show()