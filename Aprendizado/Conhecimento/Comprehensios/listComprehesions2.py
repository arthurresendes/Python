numeros = [1,2,3,4,5,6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 == 1]
print(pares)
print(impares)

# Qualquer numero par e usamos modulo de 2 da 0 e 0 em py eh False , not False = True
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)