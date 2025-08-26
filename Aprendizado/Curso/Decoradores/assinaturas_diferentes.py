def gritar(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs).upper() 
        return result
    return wrapper

@gritar
def saudacao(nome):
    return f"Olá eu sou o {nome}"

@gritar
def ordenar(principal , acompanhamento = 'batata frita'):
    return f"Gostaria de {principal} + {acompanhamento}"

print(saudacao('Arthur'))
print(ordenar("Carne parmegiana"))