import numpy as np

prices = np.array([100,200,300])
discount = np.array([0.9])
discount_prices = prices * discount
print(discount_prices)

prices1 = np.random.randint(100,500,size=(3,3))
discount1 = np.array([10,20,30])
discount_prices1 = prices1 + discount1
print(prices1)
print(discount_prices1)

array2 = np.array([1,2,3,4,5])
print(np.all(array2 > 9))      #Si todos son mayores a 9
print(np.any(array2 > 4))      #Si alguno es mayor a 4

array_a = np.array([1,2,3])
array_b = np.array([4,5,6])
concatenated_a = np.concatenate((array_a, array_a))
concatenated_ab = np.concatenate((array_a, array_b))
print(concatenated_a)
print(concatenated_ab)

#Apilar matrices vertical y horizontalmente
stacked_v = np.vstack((array_a, array_b))
print(stacked_v)

stacked_h = np.hstack((array_a, array_b))
print(stacked_h)

#Para dividir un array
array_c = np.arange(1, 10)
split_array = np.split(array_c, 3)
print(array_c)
print(split_array)