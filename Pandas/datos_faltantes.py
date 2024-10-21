import pandas as pd

dataFrame = pd.read_csv(r'F:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')

missing_data = dataFrame.isna()
print(missing_data.head(5))

missing_data_count = dataFrame.isna().sum()
print('Conteo de datos faltantes por columna:\n', missing_data_count)

#Este método elimina filas o columnas que contienen valores nulos.
no_missing_rows = dataFrame.dropna()
print('Datos sin filas con valores faltantes:\n', no_missing_rows)
#- axis=0: Elimina las filas (esto es predeterminado).
#- axis=1: Elimina las columnas.
no_missing_columns = dataFrame.dropna(axis=1)
print('Datos sin columnas con valores faltantes:\n', no_missing_columns)

#Rellenar datos faltantes
retail_data_filled_zeros = dataFrame.fillna(0)
retail_data_filled_zeros_count = retail_data_filled_zeros.isna().sum()
print(retail_data_filled_zeros_count)

#Reemplazar Datos Faltantes con Métodos Estadísticos
mean_unit_price = dataFrame['UnitPrice'].mean()
retail_data_filled_mean = dataFrame['UnitPrice'].fillna(mean_unit_price)
print(retail_data_filled_mean)
