import csv

with open('alunos.csv', 'w') as file:
    escritor = csv.writer(file)
    escritor.writerow(['nome,idade'])
    for i in range(5):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        idade = int(input(f"Digite a idade do aluno {i+1}: "))
        escritor.writerow([nome,idade])


with open('alunos.csv' , 'r') as file:
    leitura = csv.reader(file)
    next(leitura)
    for linha in leitura:
        print(linha)