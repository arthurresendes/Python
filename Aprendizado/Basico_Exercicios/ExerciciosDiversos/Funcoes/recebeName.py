def recebe(nome):
    return f"Olá, {nome}"

name = input("Digite seu nome: ").title()
print(recebe(name))