produtos = {"mouse": 50, "teclado": 120, "monitor": 900}

print(min(produtos.items(), key= lambda x: x[1]))
