numero = int(input(f"Digite um numero: "))
contador = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")