def log_args(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return wrapper

@log_args
def nome(name, idade = 18):
    return f"Meu nome é {name} e eu tenho {idade} anos"

print(nome('Arthur'))