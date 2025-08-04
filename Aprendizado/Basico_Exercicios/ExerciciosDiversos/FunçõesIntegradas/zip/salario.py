nomes = ["Guilherme", "Aline", "Vitor", "Larissa"]
salarios = [3100, 2800, 3500, 2900]
zipagem5 = zip(nomes,salarios)
mapiamento2 = map(lambda x: (x[0] , round(x[1] * 1.15)) , zipagem5)

print(list(mapiamento2))