import random

numeroSorteado  = random.randint(1,101)
numeroUser = 0
tentativas = 0

while numeroUser != numeroSorteado:
    numeroUser = int(input("Digite um numero entre 1 a 100: "))
    if numeroUser < numeroSorteado:
        print("O numero escolhido eh menor que o numero sorteado")
        tentativas += 1
    else: 
        if numeroUser > numeroSorteado:
            print("O numero escolhido eh maior que o numero sorteado")
            tentativas += 1

print(f"Parabens , voce acertou com {tentativas} tentativas e o numero sorteado era {numeroSorteado}")