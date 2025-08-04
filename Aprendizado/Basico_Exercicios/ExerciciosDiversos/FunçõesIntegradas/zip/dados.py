dados = {
    "nome": ["Ana", "Pedro", "Lucas"],
    "idade": [21, 19, 22],
    "cidade": ["SP", "RJ", "MG"]

}

print(list(zip(*dados.values())))