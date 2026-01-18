def dobro(numero: int) -> int:
    return numero * 2

print(dobro(2))

"""
Literal
Union
Final
Typed dictionaries
protocols

"""

from typing import *

def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass

def calcular(operacao: Literal['+','-'], num1:int , num2:int) -> None:
    if operacao == "+":
            print(f"{num1} + {num2} = {num1+num2}")
    elif operacao == "-":
            print(f"{num1} - {num2} = {num1-num2}")
    else:
        raise ValueError(f"Operação invalida {operacao!r}")

calcular('+',2,3)
calcular('-',2,3)

def soma(num1:int , num2:int)-> Union[str,int]:
    resultado = num1 + num2
    
    if resultado > 50:
        return f"O resultado é maior que 50:  {resultado}"
    else:
        return f"O resultado é menor que 50:  {resultado}"

print(soma(10,43))


# Não pode usar herença de pessoa
@final
class Pessoa:
    pass

class Estudante:
    pass

    # não pode sobrescrever o metodo em outra class
    @final
    def estudar(self):
        'Estou estudando'

class Estagiario:
    pass

class CursoPython(TypedDict):
    versao: str
    atualizacao: int

arthur = CursoPython(versao='4.1', atualizacao=2025)
print(arthur)

class Curso(Protocol):
    titulo: str = "Python"

def estudar(valor: Curso)-> None:
    print(f"Estou estudando o curso {valor.titulo}")

class Venda:
    titulo:str = 'Python'

v1 = Venda()
estudar(v1)