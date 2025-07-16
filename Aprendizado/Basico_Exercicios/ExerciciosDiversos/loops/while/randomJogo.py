import random

numero = random.randint(1, 20)
adivinha = 0
contador = 0

while adivinha != numero and contador < 3:

    adivinha = int(input("Voce tem 3 chances. Tente acertar o numero de 1 a 20: "))

    contador += 1


if adivinha == numero:

    print(f"Você acertou! Era o número {numero}.")

else:

    print(f"Você perdeu! O número certo era: {numero}")