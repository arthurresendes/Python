from functools import wraps

def ver_log(func):
    """Essa função log."""
    @wraps(func) # Faz aparecer o devido nome a documentação de cada devida função 
    def wrapper(*args,**kwargs):
        print(f"Você esta chamando  {func.__name__}")
        print(f"Aqui a documentação  {func.__doc__}")
        return func(*args,**kwargs)
    return wrapper

@ver_log
def soma(a,b):
    """Essa função soma dois números."""
    return a + b

print(soma.__name__)
print(soma.__doc__)
print(soma(3, 5))