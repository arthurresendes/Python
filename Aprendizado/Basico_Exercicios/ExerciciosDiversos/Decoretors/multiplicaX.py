def multiplica_por(x):
    def funcao(func):
        def wrapper(*args,**kwargs):
            return func(*args,**kwargs) * x
        return wrapper
    return funcao

@multiplica_por(10)
def numero(num):
    return num

print(numero(5))