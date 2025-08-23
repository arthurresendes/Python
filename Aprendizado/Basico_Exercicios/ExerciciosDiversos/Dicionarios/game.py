from random import choice

person1 = {'nome': 'Goblin' , 'vida' : 50 , 'ataque': 40 , 'defesa': 60}
person2 = {'nome': 'Guerreiro' , 'vida' : 100 , 'ataque': 30 , 'defesa': 60}
person3 = {'nome': 'Fantasma' , 'vida' : 70 , 'ataque': 35 , 'defesa': 80}

lista = [person1,person2,person3]
pontosUser = 0
pontosPc= 0

escolhaPc = choice((lista))

cont = 1
for personagens in lista:
    print(f"{cont}: {personagens['nome']} - Vida: {personagens['vida']} | Ataque: {personagens['ataque']} | Defesa: {personagens['defesa']}")
    cont += 1

while True:
    iterador = int(input("Digite o numero de 1 a 3: "))
    if iterador > 3 or iterador < 1:
        print("Escolha numero valido")
    else:
        break

if iterador == 1:
    escolhaUser = person1
elif iterador == 2:
    escolhaUser = person2
else:
    escolhaUser = person3

for atributos in ['vida', 'ataque','defesa']:
    if escolhaUser[atributos] > escolhaPc[atributos]:
        pontosUser+=1
    elif escolhaUser[atributos] < escolhaPc[atributos]:
        pontosPc+=1
    else:
        print("Personagens iguais")

print(f"\nResultado final:")
print(f"Usuário escolheu: {escolhaUser['nome']} - Vida: {escolhaUser['vida']} | Ataque: {escolhaUser['ataque']} | Defesa: {escolhaUser['defesa']}")
print(f"PC escolheu: {escolhaPc['nome']} - Vida: {escolhaPc['vida']} | Ataque: {escolhaPc['ataque']} | Defesa: {escolhaPc['defesa']}")
if pontosUser > pontosPc:
    print(f"{escolhaUser['nome']} venceu o {escolhaPc['nome']}!")
elif pontosUser < pontosPc:
    print(f"{escolhaPc['nome']} venceu o {escolhaUser['nome']}!")
else:
    print("Empate!")
