numeros = [1, 2, 3, 4, 5, 6]
# Use sum() com compreensão de lista para somar apenas os pares → 2 + 4 + 6 = 12
soma = sum(num for num in numeros if num % 2 == 0)
print(soma)