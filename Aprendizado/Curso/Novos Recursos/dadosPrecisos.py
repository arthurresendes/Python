def dobro(numero: int) -> int:
    return numero * 2

print(dobro(2))

"""
Literal
Union
Finaç
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