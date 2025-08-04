produtos = ["Café", "Açúcar", "Óleo", "Farinha"]
precos = [8.50, 3.40, 11.90, 6.20]
zipagem = zip(produtos,precos)
filtro = filter(lambda x: x[1] > 10, zipagem)

print(list(filtro))