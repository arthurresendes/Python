palavras = ["banana", "uva", "melancia", "pêra", "abacaxi"]

def soPala(pala):
    if len(pala) > 5:
        return pala

listagem = list(filter(soPala , palavras))
print(listagem)