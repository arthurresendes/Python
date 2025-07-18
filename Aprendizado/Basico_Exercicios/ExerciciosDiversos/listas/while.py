lista = []

produto = ""

while produto != "sair":
    produto= input("Digite o nome do produto ou 'sair: ").lower()
    if produto != 'sair':
        lista.append(produto)

print(lista)