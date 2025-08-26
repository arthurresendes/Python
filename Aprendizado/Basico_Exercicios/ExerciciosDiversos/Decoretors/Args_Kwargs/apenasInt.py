def somente_int(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance (arg,(int)):
                raise ValueError("Todos os argumentos precisam ser números!")
        return func(*args, **kwargs)
    return wrapper


@somente_int
def soma(a, b):
    return a + b


print(soma(10, 20))   # Ok
# print(soma(10, "x"))  # Vai levantar erro