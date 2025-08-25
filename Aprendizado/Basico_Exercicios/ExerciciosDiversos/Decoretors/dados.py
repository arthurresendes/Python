def autenticado(func):
    logado = True
    def wrapper():
        print("Ola")
        func()
        if logado == True:
            print("Ola seu numero eh 99999-9999")
        return func
    return wrapper


@autenticado
def ver_dados():
    print("Dados secretos")

ver_dados()