import pandas as pd

sales_data = pd.read_csv(r'F:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')

#Convertir la columna 'InvoiceDate' a tipo datetime
sales_data['InvoiceDate'] = pd.to_datetime(sales_data['InvoiceDate'])

#Eliminar filas con valores faltantes en las columnas críticas
sales_data.dropna(subset=['CustomerID', 'InvoiceDate'], inplace=True)

#Crear una nueva columna 'TotalPrice'
sales_data['TotalPrice'] = sales_data['Quantity'] * sales_data['UnitPrice']
print(sales_data.head())

#Filtrar ventas en el Reino Unido
uk_sales = sales_data[sales_data['Country'] == 'United Kingdom']
print(uk_sales)

high_quantity_sales = sales_data[sales_data['Quantity'] > 40]
print(high_quantity_sales)

uk_high_quantity_sales = sales_data[(sales_data['Country'] == 'United Kingdom') & (sales_data['Quantity'] > 40)]
print(uk_high_quantity_sales)

sales_2011 = sales_data[sales_data['InvoiceDate'].dt.year == 2011]
print(sales_2011)

sales_dec_2010 = sales_data[(sales_data['InvoiceDate'].dt.year == 2010) & (sales_data['InvoiceDate'].dt.month == 12)]
print(sales_dec_2010)