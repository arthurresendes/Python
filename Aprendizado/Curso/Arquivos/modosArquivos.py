"""
r - Leitura
w - Escrita , porém sobrescreve oque esta escrito
a - Escreve ma snão sobrescreve
x - Cria o arquivo , se já existir da erro
r+ - Leitura e escrita , arquivo deve existir
w+ - Leitura e escrita , arquivo eh criado
a+ - Leitura e escrita , appen no arquivo existente e cria se não existir

"""

valores = [1,4,50,70]
outroValores = [60,70,80,90]

with open("arquivo.txt", 'w') as file:
    for valor in valores:
        file.write(f"{valor}\n")

with open("arquivo.txt" , 'r') as file:
    conteudo = file.read()
    print(conteudo)

with open("arquivo.txt", 'a') as file:
    for valor in outroValores:
        file.write(f"{valor}\n")

with open("arquivo.txt" , 'r') as file:
    conteudo = file.read()
    print(conteudo)

def soma():
    som1 = 0
    som2 = 0
    for valor in valores:
        som1 += valor
    for valor in outroValores:
        som2 += valor
    return som1 + som2

with open("arquivo.txt" , 'a+') as file:
    file.write(f"Soma total: {soma()}\n")
    file.seek(0)
    print(file.read())

with open('newArquivo.txt' , 'w+') as file:
    while True:
        fruta = input("Digite uma fruta e se quiser sair digite sair: ").title()
        if fruta != 'Sair':
            file.write(f"{fruta}\n")
        else:
            break
    print("Lendo as frutas: ")
    file.seek(0) # Voltando para o começo do arquivo
    print(file.read())