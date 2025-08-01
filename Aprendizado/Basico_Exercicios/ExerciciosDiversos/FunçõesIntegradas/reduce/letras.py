from functools import reduce

lista = ['A','B','C']
res = reduce(lambda x , y : x + y,lista)
print(res)