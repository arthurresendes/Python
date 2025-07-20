produtos = [
    {"nome": "Arroz", "preco": 20.00},
    {"nome": "Feijão", "preco": 8.50},
    {"nome": "Leite", "preco": 5.75},
    {"nome": "Pão", "preco": 3.60},
    {"nome": "Café", "preco": 12.90}
]


print("Produto        Preço")
print("----------------------")

for item in produtos:
    print(f"{item['nome']:<15} R$ {item['preco']:.2f}")