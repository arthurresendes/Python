nomeArquivo  = input("Digite o nome do arquivo: ")

with open(nomeArquivo, 'w', encoding='UTF-8') as file:
    digita = input("Digite oque irá conter no seu arquivo: ")
    file.write(digita)

contadorVogal = 0
contadorConsoante = 0

with open(nomeArquivo, 'r', encoding='UTF-8') as file:
    conteudo = file.read()
    for letra in conteudo:
        if letra.lower() in 'aeiou':
            contadorVogal += 1
        else:
            contadorConsoante += 1

print("Vogais:", contadorVogal)
print("Consoantes:", contadorConsoante)