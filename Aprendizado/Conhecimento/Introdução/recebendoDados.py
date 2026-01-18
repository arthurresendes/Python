"""
Recebendo dados do usuario

Cast eh a conversão de 

O f antes das aspas diz "Substitua qualquer coisa dentro de chaves {} pelo valor da variável correspondente ou uma expressão."

Todo dado recebido pelo input eh tipo string

Tudo que estiver entre:
    Aspas simples
    Aspas duplas
    Aspas simples triplas
    Aspas duplas triplas
    
Exemplo:
    'Ola,mundo'
    "Hello,world"
    '''Ola, mundo'''
"""

#Entrada de dados
print("Qual eh o seu nome: ")
nome = input() #input = entrada


#Processamento
nome  = nome.title() #transforma primeira letra de cada palavra maiuscula

#Saída de dados
idade = int(input(f"Seja bem-vindo(a) {nome} , qual eh sua idade: "))
#anoNasc = 2025 - idade
print(f"Voce tem {idade} anos , assim você nasceu em {2025 - idade}")