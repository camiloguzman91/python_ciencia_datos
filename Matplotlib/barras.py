import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

categories = ['Producto A', 'Producto B', 'Producto C',]
sales = [120, 150, 90]

#Creación del gráfico de barras verticales
plt.bar(categories, sales, color=['skyblue', 'lightcoral', 'orange'], label='Ventas mensuales')

#Anotación con flecha para destacar un punto específico
plt.annotate('Máximo de ventas', xy=('Producto B', 150), xytext=('Producto C', 160), arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('Ventas de productos en un mes')
plt.xlabel('Productos')
plt.ylabel('Ventas')

#plt.legend()
plt.show()

#----------------------------------------------
#Horizontal

plt.figure(figsize=(8,6))

categories = ['Producto A', 'Producto B', 'Producto C',]
sales = [120, 150, 90]

#Creación del gráfico de barras verticales
plt.barh(categories, sales, color=['skyblue', 'lightcoral', 'orange'], label='Ventas mensuales')

plt.title('Ventas de productos en un mes')
plt.ylabel('Productos')
plt.xlabel('Ventas')

#plt.legend()
plt.show()
