def recebe(func):
    def wrapper(*args,**kwargs):
        print("Meu nome é: ")
        result = func(*args,**kwargs)
        return result
    return wrapper

@recebe
def nome_completo(name, sobrenome = 'Resende'):
    print(name)
    print(sobrenome)

nome_completo('Arthur', 'Gomes')