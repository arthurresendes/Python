matriz = [[1,2,3] , [4,5,6] , [7,8,9]]
lista = []
for linha in matriz:
    for coluna in linha:
        if coluna % 2 == 0:
            lista.append(coluna)

print(lista)