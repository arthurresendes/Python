numeros = [23, 45, 91, 62, 37]
# Ordene os números com base no último dígito.
print(sorted(numeros, key=lambda x:  x % 10))