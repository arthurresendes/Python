from collections import namedtuple as nt

produto = nt("Produto" , 'nome, preco , quantidade')

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

produto1 = produto(nome,preco,quantidade)

total = preco * quantidade
print(f"Nome: {produto1.nome}")
print(f"Preço: {produto1.preco}")
print(f"Quantidade: {produto1.quantidade}")
print(f"O total do valor foi: {total}")