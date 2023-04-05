from functools import reduce


def calcula_saldo(lancamentos) -> float:
    conta = map(lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0], lancamentos)
    saldo = reduce(lambda x, y: x - y, conta)
    return saldo