def prefixo(p):
    def funcao(func):
        def wrapper(*args,**kwargs):
            return p + " " + func(*args,**kwargs)
        return wrapper
    return funcao

@prefixo('Oi')
def nome(name = 'Arthur'):
    return name

print(nome())