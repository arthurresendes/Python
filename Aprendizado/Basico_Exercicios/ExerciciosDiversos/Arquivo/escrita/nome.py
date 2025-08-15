with open('nomes.txt' , 'a') as file:
    for nome in range(5):
        nome = input("Digite um nome: ").title()
        file.write(f'{nome}\n')

with open("nomes.txt", 'r') as file:
    print(file.read())