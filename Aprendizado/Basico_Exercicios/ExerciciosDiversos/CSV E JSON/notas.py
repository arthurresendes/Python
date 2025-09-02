import csv

with open('alunos.csv', 'w') as file:
    escritor = csv.writer(file)
    escritor.writerow(['nome','nota1','nota2'])
    for i in range(2):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        nota1 = float(input(f"Digite a nota 1 do aluno {i+1}: "))
        nota2 = float(input(f"Digite a nota 2 do aluno {i+1}: "))
        escritor.writerow([nome,nota1,nota2])

with open('alunos.csv' , 'r') as file:
    leitura = csv.DictReader(file , delimiter=',')
    for linha in leitura:
        soma = 0
        soma = float(linha['nota1']) + float(linha['nota2'])
        print(f"Aluno: {linha['nome']} | Soma: {soma} | Média: {soma/2}")