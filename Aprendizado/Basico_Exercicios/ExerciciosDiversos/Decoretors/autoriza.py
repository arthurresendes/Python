def autoriza(usuarios):
    def funcao(func):
        def wrapper(*args,**kwargs):
            if args[0] in usuarios:
                print("Acesso autorizado")
                return func(*args,**kwargs)
            else:
                return "Acesso negado"
        return wrapper
    return funcao

@autoriza(['arthur', 'maria'])
def name(nome):
    return nome

print(name('arthur'))
print(name('joao'))