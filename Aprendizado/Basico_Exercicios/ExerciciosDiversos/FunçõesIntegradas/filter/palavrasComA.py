palavras = ["fogo", "água", "terra", "ar", "vento"]

def letraA(letterA):
    for letras in letterA:
        if letras == 'a':
            return letterA

listagem = list(filter(letraA , palavras))
print(listagem)