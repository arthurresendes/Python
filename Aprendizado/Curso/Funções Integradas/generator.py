"""

"""
from sys import getsizeof

# Retorna a quantidade de bytes em memoria do elemento passado como parametro
print(getsizeof("Arthur"))

def contador():
    for i in range(3):
        yield i

gen = contador()

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
