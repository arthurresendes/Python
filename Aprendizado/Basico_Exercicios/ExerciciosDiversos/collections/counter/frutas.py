from collections import Counter

frutas = [
    "maçã", "banana", "laranja", "maçã", "uva",
    "banana", "pera", "maçã", "kiwi", "uva"
]

contador = Counter(frutas)

repetidas = {fruta: qtd for fruta, qtd in contador.items() if qtd > 1}

print("Frutas repetidas:")
for fruta, qtd in repetidas.items():
    print(f"{fruta}: {qtd} vezes")