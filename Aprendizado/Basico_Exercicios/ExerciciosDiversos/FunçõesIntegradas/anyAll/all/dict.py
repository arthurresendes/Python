alunos = [{"nome": "Ana", "nota": 8}, {"nome": "Bruno", "nota": 7.5}, {"nome": "Carlos", "nota": 8.9}]

print(all(a['nota'] > 7 for a in alunos))