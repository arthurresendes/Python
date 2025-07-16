import random
contador = 0

for i in range(1, 4):

    resposta = input("O número será ímpar ou par? ").lower()

    numeroUser = int(input("Digite o seu número: "))

    numeroRandom = random.randint(1, 100)

    total = numeroUser + numeroRandom

    print(f"Você jogou {numeroUser} e o computador {numeroRandom}. Total = {total}")

    if total % 2 == 0:

        print("Resultado: PAR")

        if resposta == "par":

            print("Você acertou!\n")

            contador += 1

        else:

            print("Você errou.\n")

    else:

        print("Resultado: ÍMPAR")

        if resposta == "ímpar" or resposta == "impar":

            print("Você acertou!\n")

            contador += 1

        else:

            print("Você errou.\n")

print(f"Você acertou {contador} de 3 rodadas.")