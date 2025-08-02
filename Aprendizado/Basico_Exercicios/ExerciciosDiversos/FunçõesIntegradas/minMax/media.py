alunos = [
    {"nome": "Lucas", "notas": [7, 8, 6]},
    {"nome": "Marina", "notas": [9, 9, 10]},
    {"nome": "Pedro", "notas": [5, 6, 5]}
]
print(min(alunos, key= lambda a: sum(a['notas'])/3))
print(max(alunos, key= lambda a: sum(a['notas'])/3))
