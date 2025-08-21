import math

def raiz(num):
    raiz = math.sqrt(num)
    if raiz == int(raiz):
        return f'A raiz quadrada é completa {raiz}'
    else:
        return 'Raiz não é completa'

print(raiz(99))