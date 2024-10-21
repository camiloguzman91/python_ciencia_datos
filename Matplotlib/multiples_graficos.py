import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = np.linspace(0, 10, 100)
y = np.sin(x)

data = np.random.randn(100)

gs = gridspec.GridSpec(2,2, height_ratios=[2,1], width_ratios=[1,1])
fig = plt.figure(figsize= (10,8))

#Primer subplot grande, ocupa toda la primera fila
ax1 = fig.add_subplot(gs[0,:])
ax1.plot(x,y, color= 'blue')
ax1.set_title('Seno de X')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')

#Segundo subplot grande, ocupa toda la primera fila
ax2 = fig.add_subplot(gs[1,0])
ax2.hist(data, bins = 20, color='purple', edgecolor='black')
ax2.set_title('Histograma')
ax2.set_xlabel('Valor')
ax2.set_ylabel('Frecuencia')

#Tercer subplot grande, ocupa toda la primera fila
ax3 = fig.add_subplot(gs[1,1])
ax3.scatter(x,y, color= 'red')
ax1.set_title('Dispersión de Seno')
ax1.set_xlabel('x')
ax1.set_ylabel('Frecuencia')

plt.tight_layout()

plt.show()
