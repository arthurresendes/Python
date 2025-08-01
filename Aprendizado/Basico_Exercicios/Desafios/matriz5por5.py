matriz = []

soma = 0

for linha in range(5):
    line = []
    for coluna in range(5):
        valor = int(input(f"Digite o valor [{linha + 1}][{coluna + 1}]: "))
        line.append(valor)
    matriz.append(line)

for linha in matriz:
    soma += sum(linha)
print(f"A média da matriz eh: {soma/25}")