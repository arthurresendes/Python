'''
Dumps - formata o doc em json no terminal apenas
dump para formatar no arquivo usando with open
load - Para ler o arquivo
loads - converte uma string json para string python

'''

import json

usuario = {
    "id": 1,
    "nome": "Arthur",
    "idade": 18,
    "email": "arthur@email.com"

}

with open('usuarios.json', 'w') as file:
    json.dump(usuario, file, indent=4)

with open('usuarios.json', 'r') as file:
    dados = json.load(file)
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")