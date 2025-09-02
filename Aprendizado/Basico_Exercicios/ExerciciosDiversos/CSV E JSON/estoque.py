import csv

with open('produtos.csv') as file:
    leitura = csv.DictReader(file, delimiter=',')
    for linha in leitura:
        estoque = int(linha['estoque']) 
        if estoque < 5:
            print(f"O produto {linha['nome']} tem apenas {estoque} unidades em estoque")