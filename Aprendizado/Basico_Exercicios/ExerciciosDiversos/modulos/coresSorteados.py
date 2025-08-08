import random

cores = ["Vermelho", "Azul", "Verde", "Amarelo", "Roxo", "Laranja"]

while True:
    inp = input("Pressione ENTER para girar a roleta letra 's' para sair!!").lower()
    if inp == 's':
        break
    cor_sorteada = random.choice(cores)
    print(f"A roleta parou na cor: {cor_sorteada}\n")