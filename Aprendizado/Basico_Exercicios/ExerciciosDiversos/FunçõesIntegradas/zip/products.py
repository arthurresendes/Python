produtos = ["Livro", "Camiseta", "Fone", "Tênis"]
precos = [18.90, 25.00, 12.00, 45.00]
zipagem8 = zip(produtos, precos)
filtro5 = filter(lambda x: x[1] > 15 , zipagem8)
mapiamento5 = map(lambda x: (x[0], x[1] - 5.0) , filtro5)

print(list(mapiamento5))