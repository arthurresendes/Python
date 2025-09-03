import json

filmes = {
    "categoria": "Ação",
    "filmes": [
        {"titulo": "Vingadores", "ano": 2012, "nota": 8.5},
        {"titulo": "Homem-Aranha", "ano": 2021, "nota": 8.7},
        {"titulo": "Batman", "ano": 2022, "nota": 8.3}
    ]
}

string = json.dumps(filmes , indent=4, ensure_ascii=False)
print(string)

for filme in filmes["filmes"]:
    print("Título:", filme["titulo"])