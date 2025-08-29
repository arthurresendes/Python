'''
Metodos é dar ação para algo
'''

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá meu nome é {self.nome} e tenho {self.idade} anos"
    
    def aniversario(self):
        self.idade += 1

p1 = Pessoa('Arthur', 18)
print(p1.apresentar())
p1.aniversario()
print(p1.apresentar())

# Metodo de classe é quando quer retornar algo fora das funções , exemplo:

class Populacao:
    cont = 0
    def __init__(self,nome):
        self.nome = nome
        Populacao.cont += 1
    
    @classmethod
    def contaPessoas(cls):
        return cls.cont

pessoas = [
    ('Arthur'),('Jose'),('Gustavo')
]

for p in pessoas:
    person = Populacao(p)
    print(person.nome)
    print(Populacao.contaPessoas())

# Metodos estaticos , @staticmethod. Serve como funções comuns não ligadas a objetos e sim a classe

class Conversor:
    def __init__(self):
        pass
    
    @staticmethod
    def celsius_para_fahrenheit(c):
        f = c * 1,8 + 32
        return f

    @staticmethod
    def fahrenheit_para_celsius(f):
        c = (f - 32) * 5/9
        return c

calcular = Conversor()
print(calcular.celsius_para_fahrenheit(25))
print(calcular.fahrenheit_para_celsius(50))