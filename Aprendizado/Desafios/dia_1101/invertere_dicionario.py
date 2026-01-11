def inverte(dicionario: dict) -> dict:
    dicionario_invertido= {}
    for chave,valor in dicionario.items():
        dicionario_invertido[valor] = chave
    return dicionario_invertido

print(inverte({'Cidade': 'São Paulo', 'País': 'Brasil'}))