import json

alunos = {
    "alunos": [
        {"nome": "Maria", "notas": [8, 7, 9]},
        {"nome": "João", "notas": [5, 6, 7]},
        {"nome": "Ana", "notas": [9, 9, 10]}
    ]

}

with open('alunos.json', 'w') as file:
    json.dump(alunos, file, indent=4)

soma = 0
with open('alunos.json', 'r') as file:
    dados = json.load(file)

for aluno in dados["alunos"]:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"{aluno['nome']} → média {media:.2f}")