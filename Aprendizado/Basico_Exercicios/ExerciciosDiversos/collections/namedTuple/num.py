from collections import namedtuple as nt

# Campos precisam ser nomes válidos (strings)
campos = ("um", "dois", "tres", "quatro", "cinco")

NovaTuple = nt("Numbers", campos)

# Criando a namedtuple
numeros = NovaTuple(1, 2, 3, 4, 5)

print(numeros)
print(numeros.tres)  # Acessando o campo "tres"