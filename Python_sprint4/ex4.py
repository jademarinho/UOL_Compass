"""
def calcular_valor_maximo(operadores, operandos):
    operacoes = []
    operacoes_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y, '%': lambda x, y: x % y}
    for op, (op1, op2) in zip(operadores, operandos):
        operacoes.append(operacoes_dict[op](op1, op2))
    return max(operacoes)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)
"""

def calcular_valor_maximo(operadores, operandos):
    resultados = list(map(lambda op, opnd: eval(f"{opnd[0]} {op} {opnd[1]}"), operadores, operandos))
    resultados_por_operador = dict(zip(operadores, resultados))
    return max(resultados_por_operador.values())

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)