import pandas as pd

dataFrame = pd.read_csv(r'F:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')

#Nombres de columnas
columns_names = dataFrame.columns
print(columns_names)

#Número de filas y columnas
num_rows, num_columns = dataFrame.shape
print('Número de filas', num_rows)
print('Número de Columnas', num_columns)

daily_Sales = dataFrame['Quantity']
print(daily_Sales)
print(daily_Sales[2])

summary = dataFrame.describe()
print(summary)

mean_value = daily_Sales.mean()
print('La media es:', mean_value)

median_value = daily_Sales.median()
print('La mediana es:', median_value)

suma = daily_Sales.sum()
print('La suma es:', suma)

count_values = dataFrame.count()
print(count_values)

daily_Sales1 = pd.Series([10,20,None,40,50])

#Suma Quantity
total_sum = daily_Sales1.sum()
print('Suma de Quantity:', total_sum)

#Conteo Quantity
count_values1 = daily_Sales1.count()
print('Conteo de Quantity:', count_values1)

muestra = dataFrame.head(8)
print(muestra)