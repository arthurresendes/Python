def so_numeros(func):
    def wrapper(*args,**kwargs):
        if all(type(arg) in [int,float] for arg in args) and all(type(valor) in [int,float] for valor in kwargs.values()):
            return func(*args,**kwargs)
        else:
            return "Só aceitamos numeros"
    return wrapper

@so_numeros
def nome(rg, idade = 18):
    return f"Meu RG é {rg} e eu tenho {idade} anos"
print(nome(555))