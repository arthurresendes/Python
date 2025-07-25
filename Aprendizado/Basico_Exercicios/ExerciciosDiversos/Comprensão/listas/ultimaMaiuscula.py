nomes = ["arthur", "pedro", "isac"]
# nome[:-1] pega todas letras menos a ultima , ja o nome[-1] pega a ultima e deixa maiuscula
resultado = [nome[:-1] + nome[-1].upper() for nome in nomes]

print(resultado)
