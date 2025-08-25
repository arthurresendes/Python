'''
Decoradores (Decoretors)

Decoretors são funções que envolvem outras funções e aprimoram seus comportamentos 

'''

print("Sem decorators: ")
def oi_tchau(func):
    def funcao():
        print('oi')
        func()
        print('tchau')
    return funcao

def nome():
    print('Arthur')

teste = oi_tchau(nome)
teste()
print("Com decorators: ")
def educacao(funcao):
    def wrapper():
        print("Foi um prazer te conhecer")
        funcao()
        print("Tenha um otimo dia")
    return wrapper() # -> colocando o () ja puxa direto a função

@educacao # Educação vira um decorator e recebe saudação como parametro
def saudacao():
    print("Seja bem-vindo")

print("\n\n")
def dormir(funcao):
    def wrapper():
        print("Vou dormir")
        funcao()
        print("Boa noite")
    return wrapper

@dormir
def name():
    print("Arthur")

name()