numeros = [-5, 3, -2, 7, -1, 0]

result = list(map(lambda n : abs(n) , filter(lambda n : n < 0, numeros)))
print(result)