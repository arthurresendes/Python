import random
numero = random.randint(1, 20)

for tentativa in range(1, 4):

    palpite = int(input(f"Tentativa {tentativa}/3 – Tente adivinhar o número de 1 a 20: "))

    if palpite == numero:

        print(f"Você acertou! Era o número {numero}.")

        break

    elif palpite < numero:

        print("O número é maior.")

    else:

        print("O número é menor.")

else:

    print(f"Você perdeu! O número correto era: {numero}")