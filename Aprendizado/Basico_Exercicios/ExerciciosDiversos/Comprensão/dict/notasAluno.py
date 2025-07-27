alunos = {"João": 7, "Maria": 9, "Lucas": 6}

newDict = {chave: valor for chave , valor in alunos.items() if valor > 7}
print(alunos)
print(newDict)