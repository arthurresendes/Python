receita = {
    'jan': 100,
    'fev': 200,
    'mar': 300
}


for i in list(receita):
    print(i)
    receita.pop(i)
    
print(receita)