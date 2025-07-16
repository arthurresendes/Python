num = 1
soma = 0

while num >= 0:

    num = int(input("Digite um numero ate ele ser negativo: "))

    if num > 0:

        soma  = num + soma

print(f"Soma dos numeros: {soma}")