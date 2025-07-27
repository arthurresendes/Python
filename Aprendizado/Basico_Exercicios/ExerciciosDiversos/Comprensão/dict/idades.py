pessoas = {'Ana': 12, 'Lucas': 18, 'Julia': 25, 'Bruno': 15}

idades = {name: ('Menor' if age < 18 else "Adulto") for name, age in pessoas.items()}

print(pessoas)
print(idades)
