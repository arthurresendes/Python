nomes = ["Rafael", "Camila", "Otávio", "Beatriz"]
salarios = [2700, 3100, 2500, 3300]
zipagem7 = zip(nomes,salarios)
filtro4 = filter(lambda x: x[1] < 3000 , zipagem7)
mapiamento4 = map(lambda x: (x[0] , x[1] * 0.9) , filtro4)

print(list(mapiamento4))