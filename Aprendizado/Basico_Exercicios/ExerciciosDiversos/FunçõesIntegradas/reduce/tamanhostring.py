from functools import reduce

palavras = ['olá', 'mundo', 'python']
res = reduce(lambda x, y: x + len(y) , palavras,0)
print(res)