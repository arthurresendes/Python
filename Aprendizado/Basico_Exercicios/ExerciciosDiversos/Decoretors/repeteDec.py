def repete(n):
    def funcao(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                print(f"Execução {i+1}")
                print(func(*args,**kwargs))
            return 'Finalizado'
        return wrapper
    return funcao

@repete(3)
def nome(name = 'Arthur'):
    return name


print(nome())