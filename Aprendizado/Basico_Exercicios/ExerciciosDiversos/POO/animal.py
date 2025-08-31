class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def falar(self):
        return f"Au au {self.nome}"

class Gato(Animal):
    def falar(self):
        return f"Miau miau {self.nome}"

an1 = Cachorro('Rex')
print(an1.falar())
an2 = Gato('Floquinho')
print(an2.falar())