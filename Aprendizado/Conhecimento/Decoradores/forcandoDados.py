def forca_tipos(*tipos):
    def decorador(func):
        def wrapper(*args,**kwargs):
            novo_args = []
            for(valor,tipo) in zip(args,tipos):
                novo_args.append(tipo(valor))
            return func(*args,**kwargs)
        return wrapper
    return decorador

@forca_tipos(str, int)
def repete_msg(msg,vezes):
    for vez in range(vezes):
        print(msg)

repete_msg('Ola',3)

def forcando_ints(*tipes): # Chamando um args para ter varios parametros e definir qual tipo de dados deve ser adicionado em tal ordem
    def decorador2(func):
        def wrapper(*args,**kwargs):
            lista = [] 
            for(valor , tipe) in zip(args,tipes):
                lista.append(tipe(valor))
            return func(*lista,**kwargs)
        return wrapper
    return decorador2


@forcando_ints(int,int)
def somando(a,repete):
    soma = 0
    for num in range(repete):
        soma = a + soma
        print(soma)

somando(10,3)