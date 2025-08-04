alunos = ["Mateus", "Júlia", "Leonardo", "Amanda"]
notas = [5.0, 6.5, 4.8, 7.3]
zipagem9 = zip(alunos,notas)
filtro6 = filter(lambda x: x[1] < 6 , zipagem9)
mapiamento6 = map(lambda x: (x[0], x[1] + 1.0) , filtro6)

print(list(mapiamento6))