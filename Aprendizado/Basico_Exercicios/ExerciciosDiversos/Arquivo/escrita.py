with open("arquivo.txt" , 'w', encoding='UTF-8') as file:
    while True:
        digite = input("Digite algo(0 para sair): ")
        if digite == '0':
            break
        else:
            file.write(f"{digite}\n")

with open("arquivo.txt", 'r') as file:
    file.seek(0)
    conteudo = file.read()
    print(conteudo)