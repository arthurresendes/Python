soma = 0
quantidade = int(input("Quantos números você quer somar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma += numero

print(f"A soma total é: {soma}")
