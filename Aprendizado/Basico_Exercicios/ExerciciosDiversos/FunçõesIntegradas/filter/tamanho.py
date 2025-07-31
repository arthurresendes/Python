palavras = ["casa", "roupa", "livro", "paz", "brisa", "vento"]

listagem = list(filter(lambda x: len(x) == 5, palavras))
print(sorted(listagem))