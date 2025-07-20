palavra = input("Digite uma palavra: ").lower()
novaPalavra = ""


for letra in palavra:
    if letra in 'aeiou':
        novaPalavra += letra.upper()
    else:
        novaPalavra += letra

print(novaPalavra)