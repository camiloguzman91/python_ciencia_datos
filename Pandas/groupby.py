import pandas as pd

df = pd.read_csv(r'F:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')

country_count = df['Country'].value_counts()
print(country_count)

country_group = df.groupby('Country')['Quantity'].sum()
print(country_group)

country_stats = df.groupby('Country')['UnitPrice'].agg(['mean', 'sum'])
print(country_stats)

country_stock_group = df.groupby(['Country', 'StockCode'])['Quantity'].sum()
print(country_stock_group)

def total_revenue(group):
    return (group['Quantity'] * group['UnitPrice']).sum()
revenue_per_country = df.groupby('Country').apply(total_revenue)
print(revenue_per_country)
