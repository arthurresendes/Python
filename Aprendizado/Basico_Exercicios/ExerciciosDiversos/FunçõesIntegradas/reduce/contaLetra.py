from functools import reduce

palavras = ['banana', 'abacate', 'uva']

res = reduce(lambda x, y: x + y .count('a') , palavras,0)
print(res)