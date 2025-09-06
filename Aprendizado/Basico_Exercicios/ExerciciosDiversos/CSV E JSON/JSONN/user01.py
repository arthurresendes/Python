import json

user = {
    "Id": 1,
    "Nome": "Arthur Resende",
    "Idade": 18
}

with open("arquivo.json", "w") as file:
    json.dump(user,file, indent=4)

with open('arquivo.json', 'r') as file:
    dados = json.load(file)
    for chave, valor in dados.items():
        if chave == "Nome":
            print(f"{chave}: {valor}")

string = json.dumps(user , indent=4, ensure_ascii=False)
print(string)
for chave , valor in user.items():
    print(f"{chave}: {valor}")