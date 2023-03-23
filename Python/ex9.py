primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, primeiroNome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[indice]
    idade = idades[indice]
    print(f"{indice} - {primeiroNome} {sobrenome} está com {idade} anos")