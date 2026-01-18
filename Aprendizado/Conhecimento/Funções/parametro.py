"""
Funções com parametro 

- Funções que recebem dados para serem processados dentro da mesma

"""

def diz_oi(nome):
    return 'Oii ' + nome

name = input("Digite seu nome: ").title()
print(diz_oi(name))

def quadrado_de_num(numero):
    return numero * numero

num = int(input("Digite um numero para ver o seu quadrado: "))
print(quadrado_de_num(num))

def cantar_parabens(aniversariante):
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print(f"Muitos anos de vida {aniversariante}")

aniversariante = input("Quem faz aniversario: ")
cantar_parabens(aniversariante)

def soma(a,b):
    return  a + b

def sub(a,b):
    return  a - b

def multi(a,b):
    return  a * b

def divide(a,b):
    return  a / b

num1 = int(input("Digite num: "))
num2 = int(input("Digite num: "))

print(soma(num1,num2))
print(sub(num1,num2))
print(multi(num1,num2))
print(divide(num1,num2)) 

def recebeTres(numero1,numero2,msg):
    return (numero1+ numero2) * msg

print(recebeTres(2,3, 'Python '))

def nome_completo(nome,sobrenome):
    return f"Ola {nome} {sobrenome}"

print(nome_completo('Arthur' , 'Resende' ))

print(nome_completo(nome='Arthur' , sobrenome='Resende'))

nome1 = 'Gus'
sobrenome1 = 'Fring'
print(nome_completo(nome = nome1 ,sobrenome = sobrenome1))
print(nome_completo(nome1,sobrenome1))

def impar(numeros):
    total = 0
    for i in numeros:
        if i %2 != 0:
            total += i
    return total

print(impar([1, 2, 3, 4, 5]))