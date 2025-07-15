palavra = input("Digite uma palavra: ").lower()
consoantes = ""

for letra in palavra:
    if letra.isalpha() and letra not in "aeiou":
        consoantes += letra

print(f"Consoantes da palavra: {consoantes}")
