def exibe_kwargs(func):
    def wrapper(*args,**kwargs):
        if kwargs:
            return func(**kwargs)
        else:
            return "Só aceitamos kwargs"
    return wrapper

@exibe_kwargs
def nome(rg, idade):
    return f"Meu RG é {rg} e eu tenho {idade} anos"
print(nome(rg = 555, idade = 18))