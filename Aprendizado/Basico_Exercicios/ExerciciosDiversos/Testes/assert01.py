from math import sqrt

def raiz_quadrada(n):
    assert n >= 0 , 'Erro, não existe raiz de 0 ou negativo'
    raiz = sqrt(n)
    return raiz

print(raiz_quadrada(25))
# print(raiz_quadrada(-3))