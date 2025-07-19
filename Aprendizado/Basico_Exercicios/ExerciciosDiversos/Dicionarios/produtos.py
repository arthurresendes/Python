produtos = [
    {
    'nome': 'Iphone',
    'preco': 2500.00
},
    {
    'nome': 'Notebook',
    'preco': 2500.00
}
]


produtos.append({'nome': 'Tenis' ,'preco': 500.00})

soma = 0

for produto in produtos:
    soma += produtos['preco']


print(f"Total dos preços: R$ {soma:.2f}")

print("Nomes dos produtos:")
for produto in produtos:
    print(produto['nome'])
