pessoas = [
{"nome": "Ana", "idade": 30},
{"nome": "Bruno", "idade": 45},
{"nome": "Carlos", "idade": 29}
]

print(max(pessoas, key=lambda p: p['idade']))