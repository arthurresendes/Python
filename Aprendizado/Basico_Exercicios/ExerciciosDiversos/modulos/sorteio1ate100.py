import random

sorteio_num = random.randint(1,101)
print("Digite um numero entre 1 até 100: ")

while True:
    try:
        num = int(input(": "))
    except:
        print("Digite um valor inteiro")
    else:
        break


if num == sorteio_num:
    print("Você acertou!!")
else:
    print("Você errou!!")

print(f"Seu num -> {num}\nRandom -> {sorteio_num}")