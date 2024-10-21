import pandas as pd

dataFrame = pd.read_csv(r'F:/Documentos/Cursos/Platzi/Python_ciencia_datos/Pandas/Online_Retail.csv',encoding='latin')
print(dataFrame)

#Son las formas más comunes de seleccionar datos.

#Iloc: ayuda a extraer la información de nuestro dataframe especificando el índice. Se utiliza para la indexación basada en enteros, permitiendo seleccionar filas y columnas por su posición.

first_row = dataFrame.iloc[0]
print(first_row)

first_five_row = dataFrame.iloc[:5]
print(first_five_row)

#subset = dataFrame.iloc[filas, columnas]
subset = dataFrame.iloc[:3, :2]
print(subset)

retail_value = dataFrame.iloc[1, 3]
print(retail_value)

#Loc: se utiliza para la indexación basada en etiquetas, permitiendo seleccionar filas y columnas por sus nombres.
print('---------------------------------------------')

row_index_3 = dataFrame.loc[3]
print(row_index_3)

row_index_0_to_4 = dataFrame.loc[0:4]
print(row_index_0_to_4)

quantity_column = dataFrame.loc[:,'Quantity']
print(quantity_column)

quantity_unitprices_column = dataFrame.loc[:, ['Quantity', 'UnitPrice']]
print(quantity_unitprices_column)