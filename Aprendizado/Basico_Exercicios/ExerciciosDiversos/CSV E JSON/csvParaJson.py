import csv
import json


with open("informacoes.csv", "a", newline='') as file:
    escritor = csv.writer(file)
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cidade = input("Digite sua cidade: ")
    escritor.writerow([nome,idade,cidade])

with open("informacoes.csv", "r") as file:
    leitura = list(csv.DictReader(file))

with open("informacoes.json", "w") as file:
    json.dump(leitura,file, indent=4)