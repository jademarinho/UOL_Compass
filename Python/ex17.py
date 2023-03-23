"""
#outro metodo de fazer, mas o udemy não aceita o NUMPY
import numpy as np

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

listas_iguais = np.array_split(lista, 3)

for lista in listas_iguais:
    print(lista)
"""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
chunk_size = 4
sublistas = [lista[i:i+chunk_size] for i in range(0, len(lista), chunk_size)]

print(*sublistas)

"""Nunca esquecer que para imprimir somente as listas e não as listas de listas, basta desempacotar usando o *"""