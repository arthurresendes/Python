def saudacao(func):
    def wrapper():
        print("Olá")
        return func()
    return wrapper

@saudacao
def nome():
    return 'Arthur'

print(nome())