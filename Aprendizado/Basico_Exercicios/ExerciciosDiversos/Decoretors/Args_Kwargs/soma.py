def somar(func):
    def wrapper(*args, **kwargs):
        print("Somando")
        result = func(*args,**kwargs)
        print(result)
    return wrapper

@somar
def number(a,b):
    return a + b

number(10,5)