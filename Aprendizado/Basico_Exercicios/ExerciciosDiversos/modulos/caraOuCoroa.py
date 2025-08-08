import random

lista_opcoes = ['cara', 'coroa']

def cara_coroa(lista, user):
    escolha = random.choice(lista)
    if escolha == user:
        return "Você ganhou!!"
    else:
        return "Você perdeu!!"

while True:
    print("Cara ou coroa: ")
    res = input(": ").lower()
    if res == 'cara' or 'coroa':
        break
    else:
        print("Digite cara ou coroa: ")
print(cara_coroa(lista_opcoes, res))