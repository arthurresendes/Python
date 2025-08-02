coordenadas = [(3, 4), (5, 12), (8, 15), (1, 1)]
print(max(coordenadas,key= lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5))