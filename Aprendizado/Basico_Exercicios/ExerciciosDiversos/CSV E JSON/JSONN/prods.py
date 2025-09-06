import json

produtos = {
    "clientes": [
        {"produto": "Cafe", "preco": 22.10, "quantidade": 3},
        {"produto": "Arroz", "preco": 11.5,"quantidade": 2},
        {"produto": "Feijão", "preco": 12, "quantidade": 1},
    ]
}

with open("prods.json", "w") as file:
    json.dump(produtos,file,indent=4)

soma = 0

with open("prods.json", "r") as file:
    dados = json.load(file)
    for item in dados["clientes"]:
        soma = soma +  (item["preco"] * item["quantidade"])
        print(f"{soma} reais do produto {item["produto"]}")