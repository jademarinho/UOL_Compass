with open('number.txt') as f:
    numeros_pares = filter(lambda x: x % 2 == 0, map(int, f))

    maiores_pares = sorted(numeros_pares, reverse=True)[:5]

    print(maiores_pares)
    print(sum(maiores_pares))

