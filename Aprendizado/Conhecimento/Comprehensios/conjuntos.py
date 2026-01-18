"""
Compreensão de conjuntos
"""

numeros = {num for num in range(1,7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)
# Dicionario
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

letras = {letra for letra in 'Arthur Resende'.upper()}
print(letras)

