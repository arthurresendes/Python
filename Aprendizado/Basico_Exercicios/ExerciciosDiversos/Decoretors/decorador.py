def repetir(n):
    def funcao(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execução {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return funcao


@repetir(3)
def oi():
    print("Oi!")

oi()