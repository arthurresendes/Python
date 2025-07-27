precos = {"banana": 3, "maçã": 5, "uva": 7}
newDict = {chave:valor * 2 for chave, valor in precos.items()}
print(newDict)