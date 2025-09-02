import csv

name = input("Digite um nome: ")

with open('alunos.csv') as file:
    leitura = csv.DictReader(file, delimiter=',')
    for linha in leitura:
        if linha['nome'] == name:
            print("Nome existente no csv")
            break
    else:
        print('Não existe')