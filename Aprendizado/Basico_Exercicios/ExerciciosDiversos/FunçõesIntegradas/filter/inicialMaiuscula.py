nomes = ["ana", "Pedro", "joao", "Lucas", "maria"]

def inicial(inicio):
    if inicio[0].isupper():
        return inicio

listagem = list(filter(inicial , nomes))
print(listagem)