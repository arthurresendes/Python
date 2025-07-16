palavra_secreta = "python"

letras_descobertas = ["_"] * len(palavra_secreta)

tentativas = 6

for tentativa in range(tentativas):

    letra = input(f"Tentativa {tentativa+1}/{tentativas} – Digite uma letra: ").lower()

    acertou = False

    for i in range(len(palavra_secreta)):

        if palavra_secreta[i] == letra:

            letras_descobertas[i] = letra

            acertou = True

    print("Palavra: " + " ".join(letras_descobertas))

    if "_" not in letras_descobertas:

        print("Parabéns! Você descobriu a palavra completa!")

        break

    if not acertou:

        print("Letra incorreta.")

else:

    print("Suas tentativas acabaram!")

    print(f"A palavra correta era: {palavra_secreta}")