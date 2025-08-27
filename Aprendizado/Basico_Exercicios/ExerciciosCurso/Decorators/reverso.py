def reverso(func):
    def wrapper():
        print("Olá")
        contrario = func()[::-1]
        return contrario
    return wrapper

@reverso
def nome():
    return 'Arthur'
print(nome())