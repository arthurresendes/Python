from functools import reduce

palavras = ['Python ', 'é ', 'muito ', 'legal']

res = reduce(lambda x, y: x + y  , palavras)
print(res)