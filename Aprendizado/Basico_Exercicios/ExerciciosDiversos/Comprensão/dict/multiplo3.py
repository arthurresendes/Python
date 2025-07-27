numeros = [3, 4, 9, 12, 15, 17]

multiplo = {num:('Multiplo de 3' if num % 3 == 0 else 'Não eh multiplo') for num in numeros}
print(multiplo)