receita = {
    'jan': 100,
    'fev': 200,
    'mar': 300
}

print(receita)

receita['abr'] = 400
receita.update({'mai': 500})
print(receita)
print("Atualizando valor de abril: ")
receita.update({'abr': 1000})
print(receita)