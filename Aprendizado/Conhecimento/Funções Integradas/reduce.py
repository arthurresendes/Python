"""
Sempre temos que importar uma biblioteca quando vai usar o reduce:
from functools import reduce

Sua estrtura:
var = reduce(funcao, iteravel)

Reduce serve para retornar um unico valor com a estrtura sendo:
def funcao(x,y):
    return x + y
resultado = reduce(funcao , [1,2,3,4]) 

Ou
resultado = reduce(lambda x,y: x + y , [1,2,3,4,5])

"""

from functools import reduce

lista_numeros = [1,2,3,4,5]
print("Vamos descobrir o fatorial de 5: ")
result = reduce(lambda x, y : x * y , lista_numeros)
print(result)

# Reduce precisa de dois parametros para retornar o valor
lista_alfabeto = ["A", "B", "C"]
result2 = reduce(lambda x , y : x + '-' + y , lista_alfabeto)
print(result2)

lista_dicionario = {'a': 10, 'b': 20, 'c': 30}
result3 = reduce(lambda x, y: x + y , lista_dicionario.values())
result4 = reduce(lambda x, y: x + " " + y , lista_dicionario.keys())
print(lista_dicionario)
print("Retornando soma do dicionario: ")
print(result3)
print("Retornando chaves do dicionario: ")
print(result4)

string = "Ola mundo adoro Phyton"
lista = string.split()
result5 = reduce(lambda x , y : x if len(x) > len(y) else y ,lista)
print(result5)