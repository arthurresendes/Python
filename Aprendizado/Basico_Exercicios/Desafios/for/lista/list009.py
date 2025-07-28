palavras = ["carro", "bicicleta", "sol", "computador", "lua", "gato"]
maiores = []

for palavra in palavras:
    if len(palavra) > 5:
        maiores.append(palavra)

print(f"Palavras com mais de 5 letras: {maiores}")
