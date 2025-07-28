palavra = input("Digite uma palavra: ")
contador  = 0

for letra in palavra:
    if letra.isdigit():
        contador += 1
   

print(f"Número de dígitos na string: {contador}")