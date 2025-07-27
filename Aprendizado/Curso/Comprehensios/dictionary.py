"""
Compreensão de dicionarios

lista = [1,2,3,4] # Lista
tupla = (1,2,3,4) # Tuple
conjunto = {1,2,3,4} # Set
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd':4} #dict

{chave: valor for chave, valor in iteravel}
"""

num = {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
quadrado = {chave: valor ** 2 for chave, valor in num.items()}

print(quadrado)

numeros = [1,2,3,4,5]
valorQuadrado = {valor: valor ** 2 for valor in numeros}
print(valorQuadrado)

chaves =  'abcde'
valores = [1,2,3,4,5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

nums = [1,2,3,4,5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in nums}
print(res)