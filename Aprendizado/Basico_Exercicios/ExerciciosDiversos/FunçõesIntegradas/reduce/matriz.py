from functools import reduce

listas = [[1, 2], [3, 4], [5]]
res = reduce(lambda x, y: x + y, listas)
print(res)