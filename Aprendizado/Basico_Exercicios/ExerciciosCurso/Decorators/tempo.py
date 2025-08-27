def imprime_inicio_fim(func):
    def wrapper():
        print('Inicio')
        func()
        print('Fim')
    return wrapper


@imprime_inicio_fim
def saudacao():
    print("Ola")


saudacao()

