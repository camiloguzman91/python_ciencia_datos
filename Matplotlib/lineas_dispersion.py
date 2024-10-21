import numpy as np
import matplotlib.pyplot as plt

month = np.array(['E', 'F', 'M', 'J', 'J'])
sales = np.array([20,25,30,28,35])

#Configurar el tamaño del gráfico
plt.figure(figsize=(8,6))

#Crear el gráfico
plt.plot(month, sales, marker='o', color='red')

plt.title('Ventas mensuales de un producto')
plt.xlabel('Meses')
plt.ylabel('Ventas en milas de unidades')

plt.show()

#-----------------------------------
#Gráfico de dispersión

#configurar el tamaño del gráfico
plt.figure(figsize=(8,6))

hours = [2,3,4,5,6,7,8]
exam = [55,60,65,70,75,80,85]

plt.scatter(hours, exam, color='green')

plt.title('Relación entre horas estudiadas y el puntaje')
plt.xlabel('Horas')
plt.ylabel('Puntaje')

plt.show()