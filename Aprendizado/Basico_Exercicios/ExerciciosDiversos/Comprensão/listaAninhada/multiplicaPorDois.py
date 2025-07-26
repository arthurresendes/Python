matriz = [[1,2,3], [4,5,6], [7,8,9]]
lista = []

for linha in matriz:
    nova_linha = []
    for coluna in linha:
        multiplica = coluna * 2
        nova_linha.append(multiplica)
    lista.append(nova_linha)

print(lista)
