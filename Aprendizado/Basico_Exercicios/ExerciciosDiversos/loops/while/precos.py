soma = 0.0
lista = []

while True:
    preco = float(input("Digite o preco da compra (0 para sair): "))
    if preco == 0.0:
        break
    else:
        lista.append(preco)

for itens in lista:
    soma += itens

print(f"Soma dos produtos: {soma}")