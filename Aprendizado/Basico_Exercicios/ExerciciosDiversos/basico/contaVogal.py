palavra = input("Digite uma palavra: ").upper()
contador = 0

for letra in palavra:
    if letra in 'AEIOU':
        contador = contador + 1


print(f"A palavra {palavra} tem {contador} vogais")