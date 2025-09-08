import math

def circuferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circuferencia.__annotations__)


class Pessoa:
    def __init__(self,nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade
    
    def andar(self) -> str:
        return f"{self.__nome} esta andando"

p = Pessoa("Arthur", 18)
print(p.__init__.__annotations__)
print(p.andar.__annotations__)