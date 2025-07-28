palavra = input("Digite uma palavra: ").lower()
contagem = {}

for letra in palavra:
    if letra.isalpha():  # considera apenas letras
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

print("Contagem de letras:")
for letra, quantidade in contagem.items():
    print(f"{letra}: {quantidade}")