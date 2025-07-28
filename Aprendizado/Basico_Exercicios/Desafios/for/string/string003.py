palavra = input("Digite uma palavra: ")
contador = 0

for letra in palavra:
    letra = letra.upper()
    print(letra)
    if letra in 'AEIOU':
        contador += 1

print(f"Número de vogais: {contador}")