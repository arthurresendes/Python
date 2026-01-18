"""
Generators são objetos iteráveis que geram valores sob demanda, usando a palavra-chave yield ou uma expressão de generator (como (x for x in iterable)).

Eles não armazenam todos os valores na memória, mas sim produzem um por vez, à medida que são solicitados (preguiçosamente).
"""
from sys import getsizeof

# Retorna a quantidade de bytes em memoria do elemento passado como parametro
print(getsizeof("Arthur"))

def contador():
    for i in range(3):
        yield i

gen = contador()

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

nomes = ['Carol', 'Carolina', 'Angelica']
print(any('C' in nome for nome in nomes))