def logar(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando função: {func.__name__}")
        print(f"  Argumentos posicionais: {args}")
        print(f"  Argumentos nomeados: {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"  Resultado: {resultado}")
        return resultado
    return wrapper


@logar
def potencia(base, expoente=2):
    return base ** expoente


print(potencia(5))
print(potencia(2, expoente=5))
