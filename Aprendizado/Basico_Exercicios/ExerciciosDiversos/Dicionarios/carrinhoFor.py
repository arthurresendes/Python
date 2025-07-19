carrinho = [
    {'nome': 'Camiseta', 'preco': 50.0, 'quantidade': 2},
    {'nome': 'Boné', 'preco': 30.0, 'quantidade': 1},
    {'nome': 'Tênis', 'preco': 120.0, 'quantidade': 1}
]

total = 0

for i in carrinho:
    subTotal = i['preco'] * i['quantidade']
    total += subTotal
    
print(f"Total do carrinho: R$ {total:.2f}")