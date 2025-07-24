def multiplica_lista(lista):
    resultado = 1
    for valor in lista:
        resultado *= valor
    return resultado


lista = []
for i in range(1, 11):
    num = int(input(f"Digite um número [{i}/10]: "))
    lista.append(num)

print("Produto dos elementos:", multiplica_lista(lista))
