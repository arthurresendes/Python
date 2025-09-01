class Funcionario:
    def __init__(self , nome: str , salario: float):
        self._nome = nome
        self._salario = salario

class Estagiario:
    def __init__(self , duracao: int):
        self._duracao = duracao

class EstagioFuncionario(Funcionario , Estagiario):
    def __init__(self , nome:str,salario: float , duracao:int):
        Funcionario.__init__(self,nome,salario)
        Estagiario.__init__(self,duracao)

    def exibir(self):
        return f'Funcionario {self._nome} com o salario de {self._salario} estagiando por {self._duracao} meses'

func1 = EstagioFuncionario('Arthur', 925.00 , 6)
print(func1.exibir())