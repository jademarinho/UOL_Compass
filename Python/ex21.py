class Passaro:
    def voar(self):
        print("Voando...")

    def som(self):
        pass

class Pato(Passaro):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def som(self):
        super().som()
        print(f"{self.nome} emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def som(self):
        super().som()
        print(f"{self.nome} emitindo som...")
        print("Piu Piu")

pato1 = Pato("Pato")
print(pato1.nome)
pato1.voar()
pato1.som()

pardal1 = Pardal("Pardal")
print(pardal1.nome)
pardal1.voar()
pardal1.som()
