class Calculadora:
    def __init__(self):
        pass
    
    def somar(self,a,b):
        return a + b

    def subtrair(self,a,b):
        return a - b
    
    def multiplica(self,a,b):
        return a * b
    
    def dividi(self,a,b):
        if b == 0:
            print("Erro")
        else:
            return a/b

calc = Calculadora()
print(calc.somar(4,5))
print(calc.subtrair(4,5))
print(calc.multiplica(4,5))
print(calc.dividi(4,2))