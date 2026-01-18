nome = input("Digite seu nome: ")

print(nome2 := input("Digite novamente: "))

cesta = []
while(fruta := input("Digite o nome de uma fruta: ")) != 'jaca':
    cesta.append(fruta)

print(cesta)