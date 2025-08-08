import random

premios = ["R$ 10", "R$ 100", "R$ 1.000", "Carro", "Viagem"]

pesos = [50, 30, 15, 4, 1]

premio = random.choices(premios, weights=pesos , k = 1)

print(premio)