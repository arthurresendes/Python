import csv

with open('alunos.csv') as file:
    leitura = csv.DictReader(file, delimiter=',')
    contador = 0
    for linha in leitura:
        contador += 1

print(f"Total de alunos cadastrados: {contador}")