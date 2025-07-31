nomes = ["ana", "joao", "bob", "maria", "arara"]

listagem = list(filter(lambda x: x[0] == x[-1], nomes))
print(sorted(listagem))