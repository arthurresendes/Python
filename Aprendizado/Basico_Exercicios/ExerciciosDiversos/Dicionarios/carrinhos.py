carrinho = []

produto1 = {
    'nome': 'Cafe',
    'preco': 9.99,
    'Quantidade':20
}

produto2 = {
    'nome': 'Caixa de bombom',
    'preco': 20.99,
    'Quantidade':10
}

produto3 = {
    'nome': 'Leite',
    'preco': 5.99,
    'Quantidade':100
}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
print(carrinho)

valorSomaTudo = 0
print("\n--- Relatório de Produtos ---")
for i, produto in enumerate(carrinho, start=1):
    total_item = produto['preco'] * produto['Quantidade']
    valorSomaTudo += total_item
    print(f"{i}. Produto: {produto['nome']}")
    print(f"   Preço unitário: R${produto['preco']:.2f}")
    print(f"   Quantidade: {produto['Quantidade']}")
    print(f"   Total do item: R${total_item:.2f}\n")

print(f"Valor total da compra: R${valorSomaTudo:.2f}")