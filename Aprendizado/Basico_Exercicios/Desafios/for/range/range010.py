maior = None  
menor = None

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if maior is None or numero > maior:
        maior = numero
# Se o maior for none ou numero for maior que o maior , maior vai receber numero
    if menor is None or numero < menor:
        menor = numero
# Se o menor for none ou numero for menor que o menor , menor vai receber numero

print(f"O maior número digitado foi: {maior}")
print(f"O maior número digitado foi: {menor}")