precos = {"banana": 2.784, "maçã": 3.14159, "uva": 1.998}

precos_arredondados = {fruta: round(valor, 2) for fruta, valor in precos.items()}
print(precos_arredondados)
