class Retangulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
         return f"A área do retangulo é: {self.altura * self.largura}"

    def perimetro(self):
        return f"O perimetro do retangulo é: {2 * (self.altura + self.largura)}"

re1 = Retangulo(5,10)
print(re1.calcular_area())
print(re1.perimetro())