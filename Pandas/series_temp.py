import pandas as pd

df = pd.read_csv(r'D:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')
print('Primeras filas del dataset original')
print(df.head())
print(df.info())

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print(df.info())

#inplace=True: Se hace la modificación directa sobre el df, no hace una copia 
df.dropna(subset=['InvoiceDate'], inplace=True)
df.set_index('InvoiceDate', inplace=True)
df['Year'] = df.index.year
df['Weekdy'] = df.index.weekday
df['Hour'] = df.index.hour
print(df['Year'])
print('Weekdy')
print(df['Hour'])
print(df)

df = df.drop(columns=['Weekdy'])
df['Weekday'] = df.index.weekday
print(df)

#Extraer información del año 2011
df_2011 = df.loc['2011']
print(df_2011.head())

df_dec_range = df.loc['2010-12-01':'2010-12-15']
print(df_dec_range.head())

#freq='D': frecuencia diaria
date_range_new = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
df_dates = pd.DataFrame(date_range_new, columns=['Date'])
print(df_dates)