"""
Funções com retorno

Quando uma função nao retorna nenhum valor , o retorno e none

Refatorar significa reescrever , redefinir
"""

from random import choice

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

def diz_ola():
    return 'ola '.title()

print(diz_ola())

pessoa = 'Arthur'
print(diz_ola() + pessoa)

# Depois do return nada é executado
def oi():
    return "oi"
    print("Estou sendo executado depois do retorno")

print(oi())

# Podemos ter diferentes returns em uma function
def new_function():
    var = True
    if var:
        return 4
    elif var is None:
        return 5
    return 'b'

print(new_function())

# Podemos aramzenar returns em variaveis 
def outra_funcao():
    return 2,3,4,5

num1, num2 ,num3 , num4  = outra_funcao()
print(num1,num2,num3,num4)

def jogar_moeda():
    escolha = input("Cara ou coroa: ").lower()
    listaEscolha = ['cara' , 'coroa']
    escolhaPc = choice(listaEscolha)
    if escolhaPc == escolha:
        return f"Você acertou!! Era {escolha}"
    else:
        return "Você errou , você é pessimo nisso"
    

print(jogar_moeda())

def eh_impar(numero):
    if numero % 2 == 0:
        return "Eh par"
    else: 
        return "Eh impar"

testeNum = int(input("Digite um numero: "))
print(eh_impar(testeNum))