matriz = [[1,2,3] , [4,5,6] , [7,8,9]]
soma = 0

for linha in matriz:
    for coluna in linha:
        soma += coluna

"""
print(sum([coluna for linha in matriz for coluna in linha]))
"""

print(soma)