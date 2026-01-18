"""
Map
Com map fazemos mapeamento de valores para função

map(função , interavel)

Exemplo:
def quadrado(n):
    retrun n * n
numeros = [1, 2, 3, 4, 5]
mapeamento = map(quadrado , numeros)
print(list(mapeamento))

Ou:
numeros = [1, 2, 3, 4, 5]
mapeamento = map(lambda x: x * x , numeros)
print(list(mapeamento))
"""

numeros = [1,2,3,4,5]
dobro = map(lambda x: x * 2 , numeros)

print(list(dobro))



palavras = ["banana", "uva", "abacaxi", "kiwi"]
quantidadeLetra = map(lambda n: len(n) , palavras)

print(list(quantidadeLetra))