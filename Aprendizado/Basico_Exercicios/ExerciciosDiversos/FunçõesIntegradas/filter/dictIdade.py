pessoas = {"Ana": 17, "Bruno": 21, "Carla": 18, "Diego": 16}


listagem = list(filter(lambda valor: pessoas[valor] >= 18  , pessoas))
print(listagem)