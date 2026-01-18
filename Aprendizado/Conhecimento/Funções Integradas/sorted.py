"""
Sorted -> Ordenação sem alterar a lista principal

sort -> Altera a principal, so funciona em lista

"""

from collections import Counter as cd

user = [
    {'username': 'Samuel', 'Tweets': ['Eu adoro bolos' , 'Eu adoro Pizza']},
    {'username': 'Carla', 'Tweets': ['Eu adoro gatos']},
    {'username': 'Jeff', 'Tweets': []},
    {'username': 'bob123', 'Tweets': []},
    {'username': 'doggo', 'Tweets': ['Vou sair hoje' , 'Eu adoro cachorros']},
    {'username': 'gal', 'Tweets': []}
]

print(sorted(user, key=lambda n: n['username']))
print(sorted(user, key=lambda n: len(n['Tweets'])))

musicas = [
    {'titulo': 'Manuel Gomes', 'tocou': 3},
    {'titulo': 'Zeca', 'tocou': 4},
    {'titulo': 'Thiaguinho', 'tocou': 5},
    {'titulo': 'Ski', 'tocou': 2}
]

print("\n")
print(sorted(musicas, key=lambda x: x['tocou'] , reverse=True))