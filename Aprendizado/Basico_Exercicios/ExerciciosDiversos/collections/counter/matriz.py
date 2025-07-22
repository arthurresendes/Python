from collections import Counter as ct

matriz = ([1,2,3] ,[2,5,6] , [5,9,8])
print(matriz)

numeros = [num for linha in matriz for num in linha]

resultado = ct(numeros)

print(resultado.most_common())