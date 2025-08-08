import random

lista_em = [1,2,3,4,5,6]
def embaralha(lista):
    random.shuffle(lista)
    return lista

print(embaralha(lista_em))

def escolhe(lista):
    res = random.choice(lista)
    return res
print(escolhe(lista_em))

def num_aleatorio(a,b):
    num = random.randint(a,b)
    return num
print(num_aleatorio(1,10))


def num_flutuante():
    num = random.random()
    return num
print(num_flutuante())


def flutuantes(a,b):
    num = random.uniform(a,b)
    return num
print(flutuantes(0.5,10.5))

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def amostra(lista,a):
    amostra = random.sample(lista,a)
    return amostra

print(tuple(amostra(lista_2,4)))