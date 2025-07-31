valores = [10, 55, 60, 45, 80, 30]

result = list(map(lambda n : n ** 2 , filter(lambda n : n > 50, valores)))
print(result)

