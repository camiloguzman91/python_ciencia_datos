import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

dates = pd.date_range(start= '2023-01-01', periods=100)

values = np.random.rand(100).cumsum()

data = pd.DataFrame({'Date': dates, 'Value': values})

#Crear gráfico de líneas
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(data['Date'], data['Value'], color= 'green')

plt.xticks(rotation=45)

plt.title('Serie de tiempo con formato en las fechas')
plt.xlabel('Date')
plt.ylabel('Value')

plt.show()

#-----------------
#Ventas mensuales

dates = pd.date_range(start= '2023-01-01', periods=12, freq='M')

sales = np.random.randint(1000, 5000, size=12)

sales_data = pd.DataFrame({'Date': dates, 'Value': sales})

plt.plot(sales_data['Date'], sales_data['Value'], marker= 'o', linestyle= '-', label= 'Ventas mensuales')

plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y')) #Para que salga el nombre de cada mes

plt.xticks(rotation=45)

plt.title('Análisis de ventas mensuales')
plt.xlabel('Date')
plt.ylabel('Sales')

plt.legend()

plt.tight_layout()

plt.show()