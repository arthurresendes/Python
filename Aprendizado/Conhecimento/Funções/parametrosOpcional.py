"""

Funções com parametros padrões

-Passagem de parametro eh opcional

"""
# Parametro obrigatorio

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
# Caso o user não preencha a potencia , por padrão vai elevar ao quadrado

def exponencial(numero, potencia = 2):
    return numero ** potencia
print(exponencial(2,3))
print(exponencial(3))

# Se voce quer passar um parametro para instrutor , voce tem que passar antes para nome

def mostra_info(nome = 'José' , instrutor = False):
    if nome == 'José' and instrutor:
        return'Bem-vindo instrutor Jose'
    elif nome == 'José':
        return "Olá José , achava que era você o instrtutor"
    else:
        return f"Ola {nome}"  
    
print(mostra_info())
print(mostra_info(True))
print(mostra_info("Arthur"))


def soma(num1,num2):
    return num1 + num2

def mat(num1,num2,fun=soma):
    return fun(num1,num2)

def subtracao(num1,num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,4,subtracao))

# Variavel global(porque não faz parte de nenhum escopo de variavel)

instrutor = 'Geek'

def diz_oi():
    # Variavel local
    instrutor = 'py'
    return f"Oi {instrutor}"

print(diz_oi())
"""
O erro é que a variavel foi inicializada fora , tendo que ser inicializada dentro da funcao
total  = 0
def erro():
    total += 1
    return total
"""
total  = 0
# O global avisa o py que quer utilizar uma variavel global
def arrumandoErro():
    global total   
    total += 1
    return total

print(arrumandoErro())

# Nonlocal serve para puxar uma variavel local de outra funcao
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()

print(fora())
