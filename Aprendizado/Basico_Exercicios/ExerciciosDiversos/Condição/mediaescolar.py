nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1+nota2+nota3)/3

if media > 6:
    print(f"Voce passou com a media: {media}")
elif media == 6:
    print("Voce ficou na media")
else:
    print(f"Voce nao passou, sua media foi: {media}")