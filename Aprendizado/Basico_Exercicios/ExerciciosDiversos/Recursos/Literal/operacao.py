from typing import *

def operacao(operador: Literal['+','-','*','/'] , num1:int , num2:int) -> Union[str,int]:
    if operador == '+':
        return f"O resultado é: {num1 + num2}"
    elif operador == '-':
        return f"O resultado é: {num1 - num2}"
    elif operador == '*':
        return f"O resultado é: {num1 * num2}"
    elif operador == '/':
        return f"O resultado é: {num1 / num2}"
    else:
        raise ValueError("Operação invalida")

print(operacao('+',5,10))
print(operacao('-',5,10))
print(operacao('*',5,10))
print(operacao('/',5,10))
#print(operacao('oi',5,10))