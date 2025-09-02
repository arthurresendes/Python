'''
Escrevendo em arquivo CSV

writer(arquivo) - para puxar uma variavel como escrita do arquivo
writerow([..,..,]) = Escreve uma linha

'''

import csv

with open('files.csv' , 'w') as file:
    escritor_csv = csv.writer(file)
    filme = None
    escritor_csv.writerow(['Titulo,Genero,Duração'])
    while filme != 'sair':
        filme = input("Informe o nome do filme(digite sair para sair): ")
        if filme != 'sair':
            genero = input("Informe o genero do filme: ")
            duracao = input("Informe a duração do filme em minutos: ")
            escritor_csv.writerow([filme,genero,duracao])
        else:
            break