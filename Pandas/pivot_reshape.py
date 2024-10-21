import pandas as pd

sales_data = pd.read_csv(r'F:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')

#Una pivot table es una herramienta para resumir y reorganizar columnas de un DataFrame de pandas, que además permite crear cálculos estadísticos (suma, conteos, promedios, etc.). Básicamente transforma los valores de determinadas filas o columnas en indices de un nuevo DataFrame, la intersección de éstos es el valor resultante.
pivot_table1 = pd.pivot_table(sales_data, values= 'Quantity', index= 'Country', columns= 'StockCode', aggfunc='sum')
print(pivot_table1)

df1 = pd.DataFrame({
    'A': ['foo', 'bar', 'baz'],
    'B': [1, 2, 3],
    'C': [4, 5, 6]
})
print(df1)

#Permite apilar (stacking) las columnas de un DataFrame. Ahora estas columnas serán filas en el DataFrame resultante. Es decir, permite pasar de un DataFrame ancho a uno largo
df_stacked = df1.stack()
print(df_stacked)

#Permite desapilar (unstacking) las filas de un DataFrame. Ahora estas filas serán columnas en el DataFrame resultante. Es decir, permite pasar de un DataFrame largo a uno ancho.

df_unstacked = df_stacked.unstack()
print(df_unstacked)