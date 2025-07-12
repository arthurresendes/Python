soma = 0
quadrado = 0

for i in range(3):
    num = float(input(f"Digite o valor {i+1}: "))
    quadrado = num * num
    soma = soma + quadrado

print(f"Soma dos valores ao quadrado eh: {soma}")