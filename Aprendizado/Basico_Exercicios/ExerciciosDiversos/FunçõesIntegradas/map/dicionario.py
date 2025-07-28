produtos = {"banana": 3, "maçã": 5, "abacate": 7}

res = map(lambda item: (item[0],item[1]* 2) , produtos.items())

print(dict(res))