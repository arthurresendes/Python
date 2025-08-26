def gritar(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs).upper() 
        return result
    return wrapper

@gritar
def saudacao(nome):
    return f"Olá eu sou o {nome}"

@gritar
def ordenar(principal = 'carne parmegiana' , acompanhamento = 'batata frita'):
    return f"Gostaria de {principal} + {acompanhamento}"

print(saudacao('Arthur'))
print(ordenar())


def verifica_argumento(valor):
    def funcao(func):
        def wrapper(*args,**kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto precisa ser {valor}"
            return func(*args,**kwargs)
        return wrapper
    return funcao

@verifica_argumento('pizza')
def comida_favorita(*args):
    return args

@verifica_argumento(10)
def soma_dez(num1,num2):
    return num1 + num2

print(soma_dez(10,2))
print(soma_dez(20,2))
print(comida_favorita('pizza', 'MC'))
print(comida_favorita('KFC', 'Parmegiana'))