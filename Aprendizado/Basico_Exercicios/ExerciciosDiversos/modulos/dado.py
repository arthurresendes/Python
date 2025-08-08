import random

def dados(num):
    dado_random = random.randint(1,6)
    if num == dado_random:
        return f"Você eh demais , o número era {num}"
    else:
        return f"Você errou, numero -> {dado_random}"

print("Digite um lado de dado de 1 a 6")
num_dado = 9
while True and num_dado > 6:
    try:
        num_dado = int(input(": "))
    except:
        print("Digite um valor inteiro")
    else:
        break

print(dados(num_dado))