import json

produtos = [
    {"nome": "Teclado", "preco": 100, "estoque": 15},
    {"nome": "Mouse", "preco": 50, "estoque": 5},
    {"nome": "Monitor", "preco": 800, "estoque": 20}
]

with open('produtos.json', 'w') as file:
    json.dump(produtos,file,indent=4)

with open('produtos.json', 'r') as file:
    dados = json.load(file)
    for p in dados:
        if p['preco'] < 150:
            print(f"{p['nome']} tem {p['estoque']} em estoque e custa {p['preco']}")