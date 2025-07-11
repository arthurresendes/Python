"""
Propostas de melhoria para a linguagem phyton

A ideia da PEP8 eh que possamos escrever codigos phyton de forma phytonica(forma bonita)
"""

"""
A primeira forma eh a correta , inicio maiusculo e sem o underline, POO
"""
class CalculadoraCientifica:
    pass


class calculadora_cientifica:
    pass

"""
Utilize nomes em minusuculos separados por underline para funcoes ou variaveis, todos metodos as baixos estão certos
"""

def soma():
    pass

def soma_dois():
    pass

numero = 4
numero_impar = 3

"""
Utilize 4 espacos para identação
"""

if 'e' in 'banana':
    print('tem')
else:
    print('nao tem')

"""
Linhas em brancos
-Seperar funções e definições de duas linhas em branco
-Metodos dentro de uma classe deve ser separado por apenas uma linha em branco
"""

class Classe:
    pass

class Outra:
    pass

#Import Errado
#import sys, os

#Import Certo
#import sys
#import os

"""
Imports devem ser colocados no topo do arquivo
"""

"""
Nunca dar espaço entre valores de função
"""
#Errado:
#funcao( algo[ 1 ], {outro: 2} )

#Certo:
#funcao(algo[1], {outro: 2})

