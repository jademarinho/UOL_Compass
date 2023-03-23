def my_map(lst, f):
    result = []
    for item in lst:
        result.append(f(item))
    return result

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def potencia(x):
    return x ** 2

nova_lista = my_map(lista, potencia)
print(nova_lista)