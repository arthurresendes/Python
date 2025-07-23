def recebeLista(lista):
    guardaNum = 0
    for item in lista:
        guardaNum += item
    return guardaNum/10

lista = []

for valor in range(1,11):
    valor = int(input("Digite um numero: "))
    lista.append(valor)

print(recebeLista(lista))

