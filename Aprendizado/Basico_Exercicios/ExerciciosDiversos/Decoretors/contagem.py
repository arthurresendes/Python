cont = 0
def contador(func):
    def wrapper():
        global cont
        print("Iremos te mostrar quantas vezes a função oi foi chamada: ")
        func()
        cont += 1
        print(cont)
        func()
        cont += 1
        print(cont)
        func()
        cont += 1
        print(cont)
        print("Funçãop oi foi chamada três vezes!!")
        return func
    return wrapper


@contador
def oi():
    print("Oi!")

oi()