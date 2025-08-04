produtos = ["Celular", "Notebook", "Tablet", "Mouse"]
precos = [1200, 3000, 1500, 80]
zipagem4 = zip(produtos,precos)
mapiamento = map(lambda x: (x[0],x[1] * 0.8) , zipagem4)

print(list(mapiamento))