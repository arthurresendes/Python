def forca_maiuscula(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs).upper()
        return result
    return wrapper

@forca_maiuscula
def nome(rg, idade):
    return f"Meu RG é {rg} e eu tenho {idade} anos"
print(nome(rg = 555, idade = 18))