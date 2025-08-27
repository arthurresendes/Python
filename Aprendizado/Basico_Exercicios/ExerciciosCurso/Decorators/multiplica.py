def multiplica_retorno(func):
    def wrapper():
        result = func() * 10
        return result
    return wrapper

@multiplica_retorno
def num():
    a = 5
    return a

print(num())