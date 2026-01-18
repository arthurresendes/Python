def sem_espacos(frases):
    nova_frase = "".join(frases.split())
    return nova_frase

def inverte_frase(frases):
    frase_invertida = frases[::-1]
    return frase_invertida

def frase_maiuscula(frases):
    maisucula = frases.upper()
    return maisucula

def recebe_frase():
    frase = input("Digite uma palavra: ")
    no_spaces = sem_espacos(frase)
    invert = inverte_frase(frase)
    maiusucula = frase_maiuscula(frase)
    print(f"Frase inicial: {frase}\nInvertida: {no_spaces}\nInvertida: {invert}\nMaiuscula: {maiusucula}")

if __name__ == "__main__":
    recebe_frase()