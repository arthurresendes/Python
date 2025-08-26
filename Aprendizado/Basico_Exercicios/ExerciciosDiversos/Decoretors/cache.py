def cache(func):
    armazenados = {} 

    def wrapper(*args, **kwargs):
        chave = (args, tuple(kwargs.items())) 
        if chave in armazenados:
            print("Pegando do cache...")
            return armazenados[chave]
        else:
            print("Calculando...")
            resultado = func(*args, **kwargs)
            armazenados[chave] = resultado
            return resultado
    return wrapper


@cache
def multiplica(a, b):
    return a * b


# Testes
print(multiplica(2, 5))  # Calcula
print(multiplica(2, 5))  # Pega do cache
print(multiplica(3, 7))  # Calcula
print(multiplica(3, 7))  # Pega do cache
