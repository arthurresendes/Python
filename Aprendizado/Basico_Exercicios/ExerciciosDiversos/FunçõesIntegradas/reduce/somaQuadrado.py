from functools import reduce

lista = [1,2,3,4]
res = reduce(lambda x , y: (x+y) **2 ,lista)
print(res)