while True:
    with open("loop.txt", 'a') as file:
        digite = input("Digite algo(0 para sair): ")
        if digite == '0':
            break
        else:
            file.write(f'{digite}\n')

with open('loop.txt', 'r') as file:
    arquivo = file.read()
    print(arquivo)