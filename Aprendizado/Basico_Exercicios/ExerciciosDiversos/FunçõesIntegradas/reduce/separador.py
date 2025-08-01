from functools import reduce

lista = [1,2,3]
res = reduce(lambda x , y : str(x) + "-" + str(y) ,lista)
print(res)