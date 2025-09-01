from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
class Quadrado(Forma):
    def __init__(self,lado):
        self.__lado = lado

    def area(self):
        return f"A area do quadrado é Lado ao quadrado: {self.__lado ** 2}"

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return f"A área do círculo é πr²:  {3.14 * self.raio ** 2}"

quadrado1 = Quadrado(4)
circulo1 = Circulo(3)

print(quadrado1.area())
print(circulo1.area())