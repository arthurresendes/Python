class Pessoa:
    def __init__(self, nome: str , idade: int):
        self. nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Sou {self.nome} e tenho {self.idade} anos.")

class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, salario: float):
        super().__init__(nome, idade)  # chama o construtor da classe mãe
        self.salario= salario
    
    def apresentar(self):  # Sobrescrevendo método
        print(f"Sou aluno {self.nome}, tenho {self.idade} anos e meu salario é {self.salario} R$.")

func1 = Funcionario('Arthur', 18, 920.00)
func1.apresentar()