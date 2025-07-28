"""
Utilizando lambdas
Conhecidas por expressões lambdas são funções sem nome , ou seja , funções anonimas

variavel = lambda argumentos: expressão

exemplo:
calculaXeY = lambda x,y : x + y

"""
quadrado = lambda x: x * x
print(quadrado(5))


verificaPar = lambda x: x %2 == 0
print(verificaPar(6))

verificaMultiplo5 = lambda x : x % 5 == 0
print(verificaMultiplo5)

comprimentoString = lambda texto: len(texto)
print(comprimentoString("ola"))

autores = ['Isac' , 'Ray' , 'Robert' , 'Arthur' , 'Frank' , 'Orson' , 'Leight']
autores.sort(key=lambda nome: nome[-1].lower())
print(autores)

def geraFuncQuadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c

teste = geraFuncQuadratica(2,3,-5)
# Passando valor de lambda
print(teste(2))