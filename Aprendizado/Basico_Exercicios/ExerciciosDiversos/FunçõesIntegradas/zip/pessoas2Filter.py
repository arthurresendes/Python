pessoas = ["Giovana", "Samuel", "Rita", "Enzo"]
idades2 = [18, 24, 20, 30]
zipagem3 = zip(pessoas,idades2)
filtro3 = filter(lambda x: x[1] >= 21 , zipagem3)

print(list(filtro3))