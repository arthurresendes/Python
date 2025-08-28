def log_nivel(n):
    def funcao(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                print(f"Eecução numero {i+1}")
                print("INFO")
            return func(*args,**kwargs)
        return wrapper
    return funcao

@log_nivel(3)
def nome(name = 'Arthur'):
    return name

print(nome())
