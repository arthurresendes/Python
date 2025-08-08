import random

contador = 0

while True:
    num = int(input("Digite um número de 1 a 20: "))
    contador += 1
    num_aleatorio = random.randint(1,21)
    if num == num_aleatorio:
        print(f"Você venceu com {contador} tentativas!!")
        break
    else:
        print("Você errou!!")

    if contador == 5:
        print("Você não conseguiu acertar, até a proxima!")
        print(f"Número -> {num_aleatorio}")
        break