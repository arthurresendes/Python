class Animal:
    def __init__(self, nome):
        self._nome = nome

    def cumprimentar(self):
        return f"Ola sou {self._nome}"
class Aquatico(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def nadar(self):
        return f"Sei nadar"
    def cumprimentar(self):
        return f"Ola sou {self._nome} do mar"

class Terrestre(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def andar(self):
        return f"Sei andar"
    def cumprimentar(self):
        return f"Ola sou {self._nome} da terra"

class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)
    def seiTudo(self):
        return f"Se andar e nadar"
    def cumprimentar(self):
        return f"Ola sou {self._nome} da terra"

tatu = Terrestre('Tat')
baleia = Aquatico('Bale')
pinguim = Pinguim('Pingui')

print(tatu.cumprimentar())
print(tatu.andar())
print(Terrestre.__mro__)
print(baleia.cumprimentar())
print(baleia.nadar())
print(Aquatico.__mro__)
print(pinguim.cumprimentar())
print(pinguim.seiTudo())
print(Pinguim.__mro__)