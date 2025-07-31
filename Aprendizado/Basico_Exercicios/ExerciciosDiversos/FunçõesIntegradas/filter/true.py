respostas = [True, False, True, False, True]

def respost(resposta):
    if resposta is True:
        return resposta

listagem = list(filter(respost , respostas))
print(listagem)