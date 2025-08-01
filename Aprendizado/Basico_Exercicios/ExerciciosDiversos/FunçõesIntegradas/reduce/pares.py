from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter (lambda x: x % 2 == 0 , nums))
res = reduce(lambda x, y: x + y , pares)
print(res)