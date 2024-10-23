import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')
print(data.info())
print(data.head())
print(data.describe())    #Métodos estadísticos

print(data.isnull().sum())
print(data.duplicated().sum())

unique_values = {col: data[col].unique() for col in data.columns}

for col, values in unique_values.items():
    print(f'Columna: {col}')
    print(f'Número de valores únicos: {len(values)}')
    print(f'Valores únicos: {values[:10]}')
    print('-' * 30)

data_cleaned = data.drop_duplicates()
data_cleaned = data_cleaned.dropna(subset=['CustomerID'])

print(data_cleaned.isnull().sum())
print(data_cleaned.duplicated().sum())

#Crear columna del precio total
data_cleaned['TotalAmount'] = data_cleaned['Quantity'] * data_cleaned['UnitPrice']

data_cleaned['InvoiceDate'] = pd.to_datetime(data_cleaned['InvoiceDate'])

data_cleaned['Year'] = data_cleaned['InvoiceDate'].dt.year
data_cleaned['Month'] = data_cleaned['InvoiceDate'].dt.month

print(data_cleaned.head())

sales_by_year = data_cleaned.groupby('Year')['TotalAmount'].sum()
print(sales_by_year)

data_cleaned['Semester'] = data_cleaned['Month'].apply(lambda x:1 if x<=6 else 2)

sales_by_semester = data_cleaned.groupby(['Year', 'Semester'])['TotalAmount'].sum()
print(sales_by_semester)

data_cleaned['Quarter'] = data_cleaned['Month'].apply(lambda x: 1 if x <= 3 else (2 if 4 <= x <= 6 else (3 if 7 <= x <= 9 else 4)))

sales_by_quarter = data_cleaned.groupby(['Year', 'Quarter'])['TotalAmount'].sum()
print(sales_by_quarter)

#Número de devoluciones
total_returns = data_cleaned[data_cleaned['Quantity'] < 0].shape[0]
print(total_returns)

total_non_returns = data_cleaned[data_cleaned['Quantity'] > 0].shape[0]
print(total_non_returns)

#Gráfica
labels = ['Devoluciones', 'No devoluciones']
sizes = [total_returns, total_non_returns]
colors = ['lightcoral', 'lightgreen']

plt.figure(figsize = (8,8))
plt.pie(sizes, labels= labels, colors=colors, startangle=140)

plt.title('Porcentaje de transacciones con y sin devolución')
plt.show()

#Gráfica de distrubución de ventas por mes y año
plt.figure(figsize=(12,6))
data_cleaned.groupby(['Year', 'Month'])['TotalAmount'].sum().plot(kind='bar')
plt.title('Distribución de ventas por mes y año')
plt.xlabel('Año, Mes')
plt.ylabel('Ventas totales')
plt.show()

#Gráfica top 10 más vendidos
top_products = data_cleaned.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(10)
top_products = top_products.reset_index() #Para tener los índices límpios
top_products = pd.merge(top_products, data_cleaned[['StockCode', 'Description']].drop_duplicates(), on='StockCode', how='left')

plt.figure(figsize=(12,8))
plt.barh(top_products['Description'], top_products['Quantity'])
plt.title('Top de productos')
plt.xlabel('Cantidad vendida')
plt.ylabel('Producto')
plt.gca().invert_yaxis()

plt.show()