string_num = "1,3,4,6,10,76"

def soma_string(string_numeros):
    numeros = string_numeros.split(",") # split na virgula
    numeros_int = [int(num) for num in numeros]
    return sum(numeros_int)

print(soma_string(string_num))