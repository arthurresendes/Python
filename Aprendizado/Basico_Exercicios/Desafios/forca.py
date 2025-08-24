palavra = 'python'
chances = 5
ganhou = False
letras_user = []

while True:
    for letra in palavra:
        if letra in letras_user:
            print(letra, end = ' ')
        else:
            print("_", end = ' ')
    tentativa = input("Letra: ").lower()
    letras_user.append(tentativa)
    if tentativa in palavra:
        print("Boa")
    else:
        chances -= 1
        print(f"Você tem {chances} chances")
    
    ganhou = True
    for letra in palavra:
        if letra not in letras_user:
            ganhou = False
    
    if chances == 0 or ganhou:
            break

if ganhou:
    print(f"Parabéns, você ganhou! A palavra era {palavra}.")
else:
    print(f"Você perdeu! A palavra era {palavra}.")