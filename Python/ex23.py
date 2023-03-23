class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

x = 4
y = 5

calculo = Calculo()

somando = calculo.soma(x, y)
subtraindo = calculo.subtracao(x, y)

print(f"Somando: {x}+{y} = {somando}")
print(f"Subtraindo: {x}-{y} = {subtraindo}")
