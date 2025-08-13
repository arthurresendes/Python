nomeArquivo  = input("Digite o nome do arquivo + o formato (nome.formato , ex: oi.txt): ")

with open(nomeArquivo, 'w', encoding='UTF-8') as file:
    digita = input("Digite oque irá conter no seu arquivo: ")
    file.write(digita)

with open(nomeArquivo , 'r' , encoding='UTF-8') as file:
    linha = file.readlines()
    print(len(linha))