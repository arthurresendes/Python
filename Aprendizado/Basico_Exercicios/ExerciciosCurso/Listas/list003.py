lista = []

for i in range(1 , 11):

    numero = int(input("Digite um numero: "))

    lista.append(numero)

for i in lista:

    if i % 2 == 0:

        print(f"{i} eh par")