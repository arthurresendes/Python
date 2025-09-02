'''
CSV - Separando valores por virgulas

reader(file) = Permite que iteramos sobre linhas
DictReader = permite que iteramos sobre linha do arquivo csv OrdereDicts, puxando no [] pelo nome da coluna do cabeçalho

'''

import os
import csv
arquivo = r"C:\Users\arthu\OneDrive\Área de Trabalho\Programação\Projetos\Python\Aprendizado\Curso\CSV e JSON\lutadores.csv"

with open(arquivo) as file:
    leitura = csv.reader(file)
    for linha in leitura:
        print(linha)

print('\n')

with open(arquivo) as file:
    leitura = csv.reader(file)
    next(leitura) # Pula a primeira linha , no caso o cabeçalho
    for linha in leitura:
        print(f"{linha[0]} nasceu em {linha[1]} e mede {linha[2]} cm")
        
        
print('\n')
print('\n')
print('\n')
with open(arquivo) as file:
    leitura = csv.DictReader(file , delimiter=',')
    for linha in leitura:
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} cm")


