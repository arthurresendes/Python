palavra = input("Digite uma palavra: ")
nova_palavra = ""

for letra in palavra:
    letra = letra.upper()
    if letra == 'A':
        nova_palavra += '*'
    else:
        nova_palavra += letra

print(f"Palavra original: {palavra}")
print(f"Palavra modificada: {nova_palavra}")