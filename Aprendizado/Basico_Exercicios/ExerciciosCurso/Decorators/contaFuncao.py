cont = 0
def conta_chamadas(func):
    def wrapper():
        global cont
        func()
        cont+=1
        func()
        cont+= 1
        print(f"A função __name__ foi chamada {cont} vezes")
    return wrapper

@conta_chamadas
def nome():
    return 'Arthur'

print(nome())

