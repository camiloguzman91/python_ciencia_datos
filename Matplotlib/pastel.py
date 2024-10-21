import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

products = ['Producto A', 'Producto B', 'Producto C',]
market_share = [50, 35, 15]

#Creación del diagrama de pastel
plt.pie(market_share, labels=products, autopct='%1.1f%%', startangle= 140, colors=['gold', 'lightcoral', 'orange'])

#Título
plt.title('Participación del mercado por producto')

#Asegurar que el gráfico sea un círculo
plt.axis('equal')

#Mostrar el gráfico
plt.show()