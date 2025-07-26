matriz = [[1, 5, 3], [4, 5, 6], [7, 5, 9]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 5:
            matriz[i][j] = 'X'

print(matriz)
