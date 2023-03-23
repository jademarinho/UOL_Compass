"""
3 inputs
Informar se é par ou impar e colocar o numero

usar range()
"""


for impar_par in range(3):
    impar_par = int(input())
    if impar_par%2 == 0:
        print(f'Par: {impar_par}')
    else:
        print(f'Ímpar: {impar_par}')

