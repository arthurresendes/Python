def conta_argumentos(**kwargs):
    contador = 0
    for chaves in kwargs.keys():
        contador += 1
    return contador

print(conta_argumentos(nome = 'a' , idade = 2))