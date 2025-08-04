alunos2 = ["Bianca", "Renato", "Fernanda", "Diego"]
notas = [6.0, 8.5, 5.9, 7.2]
zipagem2 = zip(alunos2,notas)
filtro2 = filter(lambda x: x[1] > 7.0 , zipagem2)

print(list(filtro2))