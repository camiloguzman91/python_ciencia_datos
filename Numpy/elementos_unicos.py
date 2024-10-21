import numpy as np

survey_responses = np.array(["bueno", "excelente", "malo",
                             "bueno", "malo", "excelente",
                             "bueno", "bueno", "malo",
                             "excelente"])
print(np.unique(survey_responses))

#Conteo de elementos únicos
unique_elements, counts = np.unique(survey_responses, return_counts=True)
print(unique_elements)
print(counts)

array_x = np.arange(10)
view_y = array_x[1:3]
print(array_x)
print(view_y)
array_x[1:3] = [10,11]
print(array_x)
print(view_y)

array_x = np.arange(10)
copy_x = array_x[[1,2]]
print(array_x)
print(copy_x)
array_x[1:3] = [10,11]
print(array_x)
print(copy_x)