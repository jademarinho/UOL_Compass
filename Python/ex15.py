class Lampada:
    def __init__(self, ligada): ##construtor
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

lampada1 = Lampada(True)
print(lampada1.esta_ligada())
lampada1.desliga()
print(lampada1.esta_ligada())