receita = {
    'jan': 100,
    'fev': 200,
    'mar': 300
}

print(receita)

receita.pop('mar')
print(receita)

del receita['fev']
print(receita)