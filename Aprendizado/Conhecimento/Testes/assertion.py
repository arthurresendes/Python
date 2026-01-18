'''
Assertions são afirmações

assert oq deve acontecer , mensagem de erro

'''

def calcula_media(numeros):
    assert len(numeros) != 0, 'A lista não pode estar vazia'
    return sum(numeros) / len(numeros)

print(calcula_media([10,20,30]))
# print(calcula_media([]))

def soma(a,b):
    assert a > 0 and b > 0, 'Numeros nao podem ser negativos'
    return a + b

print(soma(1,2))

def comer_fast(comida):
    assert comida in [
        'pizza',
        'MC',
        'doces',
        'batata frita'
    ], 'Comida tem que ser fast food'
    return comida

print(comer_fast('pizza'))
#print(comer_fast('BK'))