pessoas = [
    {"nome": "Ana", "idade": 22},
    {"nome": "Bruno", "idade": 19},
    {"nome": "Carlos", "idade": 25}
]
# Ordene a lista de pessoas pela idade.
print(sorted(pessoas, key= lambda p: p['idade']))