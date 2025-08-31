class Pessoa:
    def __init__(self, nome: str , idade: int):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Pessoa {self.nome} com a idade de {self.idade} anos"

class Professor(Pessoa):
    def __init__(self, nome:str,idade:int , materia: str, salario: float):
        super().__init__(nome,idade)
        self.materia = materia
        self.salario = salario
    
    def apresentar(self):
        return f"Professor {self.nome} com a idade de {self.idade} anos da materia {self.materia} com o salario de {self.salario}"

p1 = Pessoa('Arthur', 18)
print(p1.apresentar())
p2 = Professor('Alex', 48, 'Lingua Portuguesa', 9237.00)
print(p2.apresentar())