import random

lista_aleatorio_nome = []

for name in range(5):
    nome = input(f"Digite o nome {name + 1}: ")
    lista_aleatorio_nome.append(nome)

def aletorio_apresentação(lista):
    random.shuffle(lista)
    return lista
print(aletorio_apresentação(lista_aleatorio_nome))