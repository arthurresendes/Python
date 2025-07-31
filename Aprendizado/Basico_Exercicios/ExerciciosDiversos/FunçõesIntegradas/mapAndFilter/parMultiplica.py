"""
list(map(função que tera alteração, filter(oque ira filtrar , iteravel)))
"""

numeros = [1, 2, 3, 4, 5, 6]

result = list(map(lambda n : n * 2 , filter(lambda n : n % 2 == 0, numeros)))
print(result)