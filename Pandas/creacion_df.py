import pandas as pd
import numpy as np

#Data_Frame (dato bidimensional)
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
dt_from_array = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(dt_from_array)

data1 = [[1, 'José', 22],[2, 'Juan', 34],[3, 'Jimena', 25]]
df_from_list = pd.DataFrame(data1, columns=['ID', 'Name', 'Age'])
print(df_from_list)

data2 = [{'ID': 1,
          'Name': 'Juan',
          'Age': 22}]
dt_from_dict_list = pd.DataFrame(data2)
print(dt_from_dict_list)

data3 = {'ID': [1,2,3],
          'Name': ['Juan', 'Jimena', 'José'],
          'Age': [34,25,22]}
dt_from_dict = pd.DataFrame(data3)
print(dt_from_dict)

#Series: cada serie corresponde a una columna (dato unidimensional)
data4 = {'ID': pd.Series([1,2,3]),
          'Name': pd.Series(['Juan', 'Jimena', 'José']),
          'Age': pd.Series([34,25,22])}
dt_from_series_dict = pd.DataFrame(data4)
print(dt_from_series_dict)