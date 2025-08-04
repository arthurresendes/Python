alunos = ["Daniel", "Sofia", "Igor", "Manuela"]
notas = [5.5, 6.8, 7.9, 4.2]
zipagem6 = zip(alunos,notas)
mapiamento3 = map(lambda x: (x[0], x[1] + 0.5) , zipagem6)

print(list(mapiamento3))