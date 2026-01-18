"""
min- Minimo
max - Maximo


key -> Recebe uma função
"""

musicas = [
    {'titulo': 'Manuel Gomes', 'tocou': 3},
    {'titulo': 'Zeca', 'tocou': 4},
    {'titulo': 'Thiaguinho', 'tocou': 5},
    {'titulo': 'Ski', 'tocou': 2}
]

print(min(musicas, key=lambda x: x['tocou']))
print(max(musicas, key=lambda x: x['tocou']))

print(min(musicas, key=lambda x: x['tocou'])['titulo'])
print(max(musicas, key=lambda x: x['tocou'])['titulo'])