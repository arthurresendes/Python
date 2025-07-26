matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

result  = [[coluna for coluna in linha if coluna %2 == 0] for linha in matriz]

print(result)

for linha in matriz:
    for coluna in linha:
        'Matriz de outro modo'