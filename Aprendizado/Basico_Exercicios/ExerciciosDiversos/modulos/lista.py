import random

lista_nomes = ['Arthur', 'Maria', 'Jose', 'Gabriel', 'Julia']

def sorteio(lista):
    escolha = random.choice(lista)
    return f"O vencedor do sorteio foi: {escolha}"
print(sorteio(lista_nomes))