import random
contador = 0

for i in range(1, 6):

    num1 = random.randint(1, 10)

    num2 = random.randint(1, 10)

    print(f"Jogo {i}: {num1} * {num2} = ?")

    resposta = int(input("Sua resposta: "))

    multi = num1 * num2

    if resposta == multi:

        contador += 1

if contador > 3:

    print(f"Você é um gênio da matemática! Você acertou {contador} questões.")

elif contador == 3:

    print(f"Você está no caminho da matemática. Você acertou {contador} questões.")

else:

    print(f"Se esforce mais. Você acertou {contador} questões!!!")
