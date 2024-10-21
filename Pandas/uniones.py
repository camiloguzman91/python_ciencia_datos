import pandas as pd

#Crear DataFrames de ejemplo
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})
print(df1)
print(df2)

#Unión interna
inner_merged = pd.merge(df1, df2, on='key', how='inner')
print(inner_merged)

#Unión externa
outer_merged = pd.merge(df1, df2, on='key', how='outer')
print(outer_merged)

left_merged = pd.merge(df1, df2, on='key', how='left')
print(left_merged)

right_merged = pd.merge(df1, df2, on='key', how='right')
print(right_merged)

#--------------------------------------------
df3 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

df4 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5']
})
print(df3)
print(df4)

#Concatenación vertical
vertical_concat = pd.concat([df3, df4])
print(vertical_concat)

#Concatenación horizontal
horizontal_concat = pd.concat([df3, df4], axis=1)
print(horizontal_concat)

#-------------------------------------
#Join: combina dataframes con base a un índice o columna clave
df5 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

df6 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K0', 'K2', 'K3'])
print(df5)
print(df6)

joined1 = df5.join(df6, how='inner')
print(joined1)

joined2 = df5.join(df6, how='outer')
print(joined2)