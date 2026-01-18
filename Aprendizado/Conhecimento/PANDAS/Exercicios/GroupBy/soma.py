import pandas as pd

df = pd.DataFrame({
    'Loja': ['SP', 'SP', 'RJ', 'RJ', 'MG', 'MG'],
    'Categoria': ['Eletrônico','Eletrônico','Eletrônico','Móveis','Móveis','Móveis'],
    'Vendas': [1000, 1500, 2000, 500, 800, 700]
})

result = df.groupby(['Loja', 'Categoria'])['Vendas'].sum()
print(result)