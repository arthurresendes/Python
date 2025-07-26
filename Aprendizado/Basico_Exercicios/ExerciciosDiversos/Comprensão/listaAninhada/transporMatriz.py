matriz = [[1,2,3], [4,5,6], [7,8,9]]

transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print(transposta)
