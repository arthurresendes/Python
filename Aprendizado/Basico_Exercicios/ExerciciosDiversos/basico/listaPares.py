lista = []

for i in range(1, 11):
    numero = int(input(f"Digite um numero: "))
    lista.append(numero)

print(lista)

listaPar = []

for i in lista:
    if i % 2 == 0:
        listaPar.append(i)

print(listaPar)