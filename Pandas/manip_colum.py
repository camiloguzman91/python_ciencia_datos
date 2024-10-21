import pandas as pd

df = pd.read_csv(r'D:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')
print(df)

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print(df.head())

df['HighValue'] = df['TotalPrice'] > 16
print(df['HighValue'].head)

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print(df.info())

df['DiscountedPrice'] = df['UnitPrice'].apply(lambda x: x * 0.9)
print(df.head(3))

def categorize_price(price):
    if price > 50:
        return 'High'
    elif price >= 20:
        return 'Medium'
    else:
        return 'Low'
    
df['PriceCategory'] = df['UnitPrice'].apply(categorize_price)
print(df.head(3))